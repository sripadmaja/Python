#to create a strong password:
import random
import string
ascii1=string.ascii_lowercase
ascii2=string.ascii_uppercase
lowercase=list(ascii1)
uppercase=list(ascii2)
numberchars=['1','2','3','4','5','6','7','8','9','0']
specialchars=['!','@','#','$','%']
password1=random.choice(lowercase) + random.choice(uppercase) + random.choice(numberchars) + random.choice(specialchars)
password2=random.choice(lowercase) + random.choice(uppercase) + random.choice(numberchars) + random.choice(specialchars)

password=password1+password2
print(password)
    
