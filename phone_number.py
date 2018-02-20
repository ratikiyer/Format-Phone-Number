phone_number = ("5104062439")


if not phone_number.isnumeric():
    print ("Error. Please enter numbers only.")
elif len(phone_number) != 10:
    print ("Error. A valid phone number should have 10 digits.")
else:
    v = "(" + phone_number[0:3] + ")-" + phone_number[3:6] + "-" + phone_number[6:10]
    print (v)
