# Amarjit Maan
# COS 205, Python Programming
# Problem # 4

odometer_last_reading = int(input("Input the reading of the odometer: "))

# Initiate the final sum as 0
finalSum = 0

#Initiate the legs reading equal to 0
legs = 0

# Use while loop to ask the user for odometer reading and gas consumed at each leg
while True:
    # Ask user to enter the odometer reading and gas consumed
    inp = str(input("Enter both the odometer reading and gas_Value consumed(seperated by comma) : "))
    if inp.strip("") == "":
        break
    else:
        #Split the inputs accordingly
        #Split the entered values
        input_fields = inp.split(",")
        odometer = eval(input_fields[0])
        gas_value = eval(input_fields[1])

        #Print the vaules using print statement
        print("The MPG value is :", (odometer - odometer_last_reading) / gas_value)
        finalSum = finalSum + ((odometer - odometer_last_reading) / gas_value)
        legs = legs + 1
        odometer_last_reading = odometer

#Print the miles per gallon for whole trip
print("The final value is: ", finalSum / legs)
