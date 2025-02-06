# print("hello,world!")
# print("my name is amin ebrahimi")
# print(3+5)

# name="amin"
# age=25
# height=1.75
# is_student=True
# print(name)
# print(age)
# print(height)
# print(is_student)


##string
# greeting="hello,world!"
# print("hello,wolrd!")
# print(greeting)

##Boolean  (true or false)

##list   same my daten
# my_list=[1,2,3, "amin, true"]
# print(my_list)

##Dictionary
# my_dict={"name":"amin"  ,  "age":25 , "height":1.85}
# print(my_dict)

# x=5
# y=10
# ##عملگرهای ریاضی:
# print(x+y)
# print(x-y)
# print(x*y)
# print(x/y)
# print(x//y)     # تقسیم صحیح
# print(x%y)      # باقی‌مانده
# print(x**y)     # توان

##عملگرهای مقایسه‌ای
# a=10
# b=5

# print(a==b)     # برابر است؟
# print(a!=b)     # نابرابر است؟
# print(a>b)
# print(a<b)
# print(a>=b)
# print(a<=b)
     
#عملگرهای منطقی
# x=True
# y=False

# print(x and y)
# print(x or y)
# print(not x)
# print (not y)

##ubung 1 :یک متغیر تعریف کنید که سن شما را ذخیره کند، سپس آن را چاپ کنید.
# age_amin=35
# print(age_amin)
# print(35)

# ################ubung 2:یک لیست از سه علاقه‌مندی خود بسازید و آن را چاپ کنید.
#  my_list = [" 1:"footbal" , 2:"basketball" , 3:"volleyball","]
# my_list= ["football","basketball","volleyball"]   
# print(my_list)
# print("mylist",my_list)

##ubung 3:برنامه‌ای بنویسید که دو عدد از کاربر بگیرد، آن‌ها را جمع کند و نتیجه را چاپ کند. (راهنما: از input() استفاده کنید)
# number1=input("please enter a number1:")
# number1=float(number1)
# # number1=int(number1)

# number2=input("please enter a number2:")
# number2=int(number2)

# result=number1 + number2
# print("result:",result)

# ########ubung 4 : selbst
# num1=input("please enter a number1:")
# num1=int(num1)

# num2=input("please enter a number2:")
# num2=int(num2)

# num3=input("please enter a number3:")
# num3=float(num3)

# result1=num1+num2+num3
# result2=num1==num2==num3
# result3=num1!=num2!=num3

# print("result1:",result1)
# print("result2:",result2)
# print("result3:",result3)

#درس 4 :ساختار کنترلی استفاده از  if , elif , else
# age= input("please enter your age: ")
# age=int(age)
# if age < 18:
#     print("ypu are child")
# elif age <50:
#     print("you are young")
# else:
#     print("you are old")


####### For Loop
# name=["Amin" , "sanaz" , "aaa"]

# for name in name:
#     print(f"salam:{name}")

    
 ##مثال: استفاده از range()
# for i in range(1,10):
#      print(i)
       
# class Car:
#      def __init__(self , model, color):
#           self.model=model
#           self.color=color
          
#      def intriduce(self):
#           return f"this {self.model}has a {self.color}color."

# car1=Car("BMW" , "RED")
# print(car1.intriduce())

# class Number:
#      def __init__(self, num1 , num2):
#           self.num1=num1
#           self.num2=num2
          
#      def add(self):
#           return f"sum is {self.num1 + self.num2}"
     
# p1=Number(5,8)
# print(p1.add())

# class Regtangle:
#      def __init__(self , height , width):
#           self.height=height
#           self.width=width
#      def area(self):
#           return f"area is {self.height * self.width}"
#      def preimeter(self):
#           return f"premiter is {2*(self.height + self.width)}"
     
# area1=Regtangle(10,30)
# print(area1.area())
# print(area1.preimeter())


