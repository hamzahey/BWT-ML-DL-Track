def convert_temperature(temp, scale):
    # Check the scale and convert the temperature accordingly
    if scale.upper() == "C":
        converted_temp = (temp * 9/5) + 32
        print(f"{temp}°C is {converted_temp:.2f}°F")
        return converted_temp
    elif scale.upper() == "F":
        converted_temp = (temp - 32) * 5/9
        print(f"{temp}°F is {converted_temp:.2f}°C")
        return converted_temp
    else:
        print("Invalid scale provided. Use 'C' for Celsius or 'F' for Fahrenheit.")
        return None

# Example usage
temperature = float(input("Enter the temperature value: "))
scale = input("Enter the scale (C for Celsius, F for Fahrenheit): ")
converted_temperature = convert_temperature(temperature, scale)
