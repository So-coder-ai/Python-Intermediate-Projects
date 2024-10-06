import sys
import requests
from PyQt5.QtWidgets import (QApplication , QWidget ,QLabel 
                             ,QLineEdit , QPushButton, QVBoxLayout)
from PyQt5.QtCore import Qt
class WeatherApp(QWidget):
   def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter City Name: ",self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather",self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.initUI()

   def initUI(self):
        self.setWindowTitle("Weather App")

        vbox = QVBoxLayout()

        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)
        self.setLayout(vbox)
        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)


        self.city_label.setObjectName("city_label")
        self.emoji_label.setObjectName("emoji_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.description_label.setObjectName("description_label")

        self.setStyleSheet(
            """
        QLabel,QPushButton
        {
        font-family: calibri;
        }

        QLabel#city_label
        {
        font-size: 40px;
        font-weight:italic
        
        }

        QLineEdit#city_input
        {
        font-size: 40px;
        }
        QPushButton
        {
        font-size: 30px;
        font-weight:bold;
        }

        QLabel#temperature_label
        {
        font-size: 75px;
        }
        
        QLabel#emoji_label
        {
            font-size: 100px;
            font-family: Segoe UI emoji;
        }
        QLabel#description_label
        {
        font-size: 40px;
        }
"""
        )

        self.get_weather_button.clicked.connect(self.get_weather)

   def get_weather(self):
        api_key ="15efa8fd36c40de76adcd8f8b7164642"
        city = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
        
            if data["cod"] == 200:
                self.display_weather(data)
        except requests.exceptions.HTTPError:
           match response.status_code:
                case 400:
                  self.display_error("Bad request \n Please check your input")
                case 401:
                   self.display_error("unauthorized \n invalid api key")   
                case 403:
                  self.display_error("FOrbidden\n access is denied")
                case 404:
                   self.display_error("Not Found\n city not found")
                case 500:
                  self.display_error("INternal server error \n please try again later")
                case 502:
                  self.display_error("Bad gateway \n invalid response from server")
                case 503:
                  self.display_error("service unavailable \n server is down ")
                case 505:
                  self.display_error("gateway time out \n no response from the server")
                case _:
                  self.display_error(f"HTTP error occured \n http_error")
        except requests.exception.ConnectionError:
               self.display_error("connection Error:\n check your internet connection")
        except requests.exception.Timeout:
               self.display_error("Timeout Error:\nthe request timed out")
        except requests.exception.TooManyRedirects:
               self.display_error(" Too many redirects :\ncheck the url")
        except requests.exceptions.RequestException as req_error:
            self.display_error(f"request error :\n{req_error}")



   def display_error(self,message):
        self.temperature_label.setStyleSheet("font-size: 30px;")
        self.temperature_label.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()

   def display_weather(self,data):

      temperatur_k = data["main"]["temp"]
      temperatur_c = temperatur_k - 273.15
      self.temperature_label.setStyleSheet("font-size: 75px;")
      self.temperature_label.setText(f"{temperatur_c:.0f}°C")
      weather_id = data["weather"][0]["id"]
      self.emoji_label.setText(self.get_weather_emoji(weather_id))
      weather_description = data["weather"][0]["description"]
      
      self.description_label.setText(weather_description)
      self.description_label.setStyleSheet("font-size: 60px;")


   @staticmethod
   def get_weather_emoji(weather_id):
      if 200 <= weather_id <= 232:
           return "⛈️"
      elif 300 <= weather_id <= 321:
          return "🌦️"
      elif 500 <= weather_id <=531:
          return "🌧️"
      elif 600 <= weather_id <=622:
          return "❄️"
      elif 701 <= weather_id <= 741:
          return "🌫️"
      elif weather_id ==762:
           return "🌋"
      elif weather_id == 771:
          return "💨"
      elif weather_id == 781:
          return "🌪️"
      elif weather_id == 800:
          return "🌞"
      elif 801 <= weather_id <= 804:
          return "☁️"
      else:
          return ""
         
if __name__ == "__main__":
    app = QApplication(sys.argv)
    weatherapp = WeatherApp()
    weatherapp.show()
    sys.exit(app.exec_())