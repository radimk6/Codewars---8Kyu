# Write function bmi that calculates body mass index (bmi = weight / height2).

# if bmi <= 18.5 return "Underweight"

# if bmi <= 25.0 return "Normal"

# if bmi <= 30.0 return "Overweight"

# if bmi > 30 return "Obese"

weight = input("Zadejte svoji váhu v kg: ")
height = input("Zadejte svoji výšku v m: ")

def bmi(weight, height):
    bmi = float(weight) / (float(height) ** 2)
    if bmi <= 18.5:
        return "Underweight"
    elif bmi <= 25:
        return "Normal"
    elif bmi <= 30:
        return "Overweight"
    else:
        return "Obese"
    
print(bmi(weight, height))
    
#   BMI = float(Váha) / (float(Výška)**2)

# print("Vaše BMI je", BMI)

# if BMI < 18.5:
#   print("Máte podváhu")
# elif BMI >= 18.5 and BMI < 25:
#   print("Máte ideální váhu")
# elif BMI >= 25 and BMI < 30:
#   print("Máte nadváhu")
# else:
#   print("Jste obézní")