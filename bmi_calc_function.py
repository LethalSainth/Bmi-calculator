def bmi_calc(weight, height):

    if (weight.isnumeric() & height.isnumeric()):
        weight = float(weight)
        height = float(height)

        bmi = (weight/(height**2)) * 10000

        if bmi < 18.5:
            result = "UNDERWIGHT!!!!"
        
        elif bmi >= 18.5 and bmi < 24.9 :
            result = bmi,'HEALTHY!!!!'
            
        elif bmi >= 25 and bmi < 29.9 :
            result = bmi,'OVERWEIGHT!!!!'

        elif bmi >= 30 and bmi <= 39.9 :
            result = bmi, 'OBESE!!!!'

        else: 
            result = 'SEVERE OBESEITY!!!!'
    

    else:
        result = "Please enter a valid number for Weight and Height."

    return result

print(bmi_calc('95','197'))