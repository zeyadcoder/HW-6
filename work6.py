def check_age(age_input):
    try:
        # Convert input to integer
        age = int(age_input)

        # Check if the age is within a reasonable range (0-120)
        if age < 0 or age > 120:
            return "Error: Age entered is out of a valid range (0-120)."
        
        # Check if the age is even or odd
        if age % 2 == 0:
            return f"Age {age} is valid and even."
        else:
            return f"Age {age} is valid and odd."