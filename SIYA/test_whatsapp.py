import pywhatkit as kit
number = input("Enter number here:")
name = input("Enter message  here:")
print("Remember to enter time in 24 hour clock")
time = int(input("enter hour here:"))
minn = int(input("enter minute here:"))
kit.sendwhatmsg("+91"+number, name, time, minn)
