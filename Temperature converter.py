'''Temperature Converter'''

def celsius_to_fahrenheit(celsius):
    #Convert celsius to fahrenheit..
    return(celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    #Convert fahrenheit to celsius..
    return(fahrenheit - 32) * 5/9

def main():
    #Main function to run the temperature conversion program..

    print("\nTemperature conversion program:\n")
    print("1. convert celsius to fahrenheit")
    print("2. convert fahrenheit to celsius")


    while True:
        #Ask the user to choose the conversion type..
        choice = input("\nEnter your choice(1/2): ")

        if choice == '1':
            # convert celsius to farenheit..
            try:
                celsius = float(input("\nEnter temperature in celsius: "))
                fahrenheit = celsius_to_fahrenheit(celsius)
                print(f"{celsius}*c is equal to {fahrenheit}*f")
           
            except ValueError:
                print("\nPlease enter a valid number.")

        elif choice == '2':
            #convert Fahrenheit to Celsius..
            try:
                fahrenheit = float(input("\nEnter temperature in Fahrenheit: "))
                celsius = fahrenheit_to_celsius(fahrenheit)
                print(f"{fahrenheit}*f is equal to {celsius}*c")

            except ValueError:
                print("\nPlease enter a valid number.")

        else:
            print("\nInvalid choice. Please select either 1 or 2.")

        # Ask the user if they want to perform another conversion..
        another_conversion = input("\nDo you want to perform another conversion? (yes/no): ").lower()

        if another_conversion != 'yes':
            print("\nThank you for using the temperature conversion program. GOODBYE!!")
            break

if __name__ == "__main__":
    main()