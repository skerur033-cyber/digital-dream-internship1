p_price = 10000
gst =0.18 * p_price
t_bill = p_price + gst
print("Total bil with gst:", t_bill)


t_students = 30
groups = 7
remainder = t_students % groups
print("remind student:", remainder)

age = 19
print("Eligible to vote:", age >= 18)

salary1 = 10000
salary2 = 20000
print("Empl earns more :", salary1 > salary2)

pin_enter = 143
pin_save = 143
print(" login pin enterd :", pin_enter == pin_save)

marks = 55
attendance = 80
print("Pass:", marks > 40 and attendance > 75)

user_name = False
email_valid= True
print("Login allow:", user_name  or email_valid)

marks=50
attendance=80
print("pass: ",marks > 40 and attendence > 70)

user= False
email=True
print("allow login:" ,user and email)

suspend=True
print("access for suspend:", not suspend)


wellet=5000
wellet-=500
print("wellet balence:",wellet)

score=10
score+=5
print("game score:",score)

stock = 100
sales = 20
stock -= sales
print("Remaining stock:", stock)

a = 5  
b = 3  

print("a & b:", a & b)  
print("a | b:", a | b)  

num = 4
print("Left shift:", num << 1)  
print("Right shift:", num >> 1)

students_list = ["Rahul", "Priya", "Shankar", "Amit"]
print("Is Shankar present?", "Shankar" in students_list)
inventory = ["Laptop", "Mouse", "Keyboard"]
print("Is Monitor available?", "Monitor" in inventory)

x = [1, 2, 3]
y = [1, 2, 3]
z = x

print("x is y:", x is y)       
print("x is z:", x is z)      
print("x is not y:", x is not y)