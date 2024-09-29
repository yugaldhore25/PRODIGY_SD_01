print("TASK:-1"'\n')
print("This code is represented by Yugal Dhore"'\n')
print("--------TEMPERATURE CONVERSION PROGRAM-------"'\n' )
#ENTER TEMPERATURE AND UNIT.
temperature = float(input("Enter value of Temperature with unit: "))
org_unit=input("Enter value the original unit of measurement i.e (C for Celsius, F for Fahrenheit, K for Kelvin): ")
#MAIN FUNCTION,
def main():
    if org_unit == 'C':
        Celsius = temperature
        Fahrenheit = Celsius_to_Fahrenheit(Celsius)
        Kelvin = Celsius_to_Kelvin(Celsius)
        print(f"{Celsius} Celsius is equal to {Fahrenheit} Fahrenheit and {Kelvin} kelvin.")
    
    elif org_unit == 'F':
        Fahrenheit = temperature
        Celsius = Fahrenheit_to_Celsius(Fahrenheit)
        Kelvin = Fahrenheit_to_Kelvin(Fahrenheit)
        print(f"{Fahrenheit} Fahrenheit is equal to {Celsius} Celsius and {Kelvin} Kelvin.")
    
    elif org_unit == 'K':
        Kelvin = temperature
        Celsius = Kelvin_to_Celsius(Kelvin)
        Fahrenheit = Kelvin_to_Fahrenheit(Kelvin)
        print(f"{Kelvin} Kelvin is equal to {Celsius} Celsius and {Fahrenheit} FahrenheitS.")
    
    else:
        print("Invalid unit of Measurement or Check the value.")

#CONVERSION
def Celsius_to_Fahrenheit(Celsius):
    return (Celsius * 9/5) + 32

def Celsius_to_Kelvin(Celsius):
    return (Celsius + 273.15)

def Fahrenheit_to_Celsius(Fahrenheit):
    return (Fahrenheit - 32) * 5/9

def Fahrenheit_to_Kelvin(Fahrenheit):
    return (Fahrenheit - 32) * 5/9 + 273.15

def Kelvin_to_Celsius(Kelvin):
    return (Kelvin - 273.15)

def Kelvin_to_Fahrenheit(Kelvin):
    return (Kelvin - 273.15) * 9/5 + 32

if __name__ == '__main__':
    main()
