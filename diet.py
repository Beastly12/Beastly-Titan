print("I AM A BMI CALCULATOR AND A DIET GUIDE")

name=(input('what is your name ?  '))

print('HI', name ,'IM BEASTLY!!!!')

weight= float(input('PLEASE INPUT YOUR WEIGHT IN KG AND PRESS ENTER:    ' ))
height = float(input('PLEASE INPUT YOUR HEIGHT IN METERS:        '))

bmi = weight/(height**2)

print( name,  'Your BMI is: ' , bmi )

if ( bmi< 16):
   print ('You are severly underweight and quite unhealthy.' )
   print ('Do not panic :) ', name )
   print(" I would recommend you go on a 'HIGH CARB DIET' because it is  highly recommended by 9 out of 10 Doctors to help with weight gain .   ")
   
   print(f""" Breakfast:: 2 Boiled Eggs + Banna + Water or Oatmeal with Friuts           Lunch:: Goat Meat Pepper soup or Beans pottage(no oil)              Dinner:: 1 Large bowl of watermelon or Chicken peppersoup with Vegetables      """)



elif (bmi>=16 and bmi< 18.5 ):
    print(name,  'You are underweight, you need to stay on a well Balanced and Eat well diet. ') 
    print('  please give me some time  ',name ) 
    print(f""" Breakfast:: 2 Boiled Eggs + Banna + Water or Oatmeal with Friuts           Lunch:: Goat Meat Pepper soup or Beans pottage(no oil)              Dinner:: 1 Large bowl of watermelon or Chicken peppersoup with Vegetables      """)


elif (bmi>=18.5 and bmi < 25):
    print('You are Healthy',name,', you are on a good diet  :) .   ')
    print(' You do not need a new Diet  ')


elif (bmi >= 25 and bmi < 30):
    print('You are Overweight ', name ) 
    print('    Recommended diets ::   Keto Diet ,Dukan Diet(weight loss) etc.  ')
    print('  please give me some time  ',name ) 

    print(f""" Breakfast:: 2 Boiled Eggs + Banna + Water or Oatmeal with Friuts           Lunch:: Goat Meat Pepper soup or Beans pottage(no oil)              Dinner:: 1 Large bowl of watermelon or Chicken peppersoup with Vegetables      """)

elif(bmi>=30):
    print('   You are severely over weight',name,' which is unhealthy. ')
    print('  Recommended Diet:: Paleo Diet , Vegan Diet , low-Carb Diet.   ')
    print('  please give me some time  ',name )

    print(f""" Breakfast:: 2 Boiled Eggs + Banna + Water or Oatmeal with Friuts           Lunch:: Goat Meat Pepper soup or Beans pottage(no oil)              Dinner:: 1 Large bowl of watermelon or Chicken peppersoup with Vegetables      """)


print('Thank You for using BEASTLY.')
print('GOOD BYE !!!', name )