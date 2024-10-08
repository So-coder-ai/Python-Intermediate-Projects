# remove any '-' or ' '
# add all digits in the odd places from right to left
#double every second digit from right to left 
#if result is a two digit number 
#add the two digit number together to get a single digit
#sum the total of steps 2 and 3
# if the sum is fivisible by 10 the credit card is valid 
#sample 1. 4242424242424242
#sample 2. 4000056655665556
sum_odd_digits = 0
sum_even_digits =0
total = 0

card_number = input("enter a credit card :")
card_number = card_number.replace("-","")
card_number = card_number.replace(" ","")
card_number = card_number[::-1]
for x in card_number[::2]:
    sum_odd_digits += int(x)
for x in card_number[1::2]:
    x = int(x)*2
    if x >= 10:
        sum_even_digits += (1+(x%10))
    else:
        sum_even_digits += x

total = sum_odd_digits + sum_even_digits
if total%10 == 0:
    print("valid!!")
else:
    print("invalid!!")
