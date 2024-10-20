def calculate_bmi(height, weight):
    
    # Display height and weight
    print("Height = " + str(height) + " meters")
    print("Weight = " + str(weight) + " kg")
    
    # Calculate BMI
    bmi = weight / (height ** 2)
    
    # Display calculated BMI
    print("Calculated BMI = " + str(round(bmi, 2)))
    
    # Determine weight classification based on BMI
    if bmi < 18.5:
        print("Weight Classification: Under Weight")
    elif 18.5 <= bmi <= 25.0:
        print("Weight Classification: Normal Weight")
    else:
        print("Weight Classification: Over Weight")

# Call the function
calculate_bmi(weight=57, height=1.73)
