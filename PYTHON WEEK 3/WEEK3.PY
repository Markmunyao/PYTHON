marks= 80
result= ""
if marks < 30:
    result="umeuma nje"

elif marks>70:
    result ="passed  with dinstiction"
else:
    result="passed"   
print(result)  

def checkvowel(n):
    match n:
        case 'a': return "vowel alphabet"
        case 'e': return "vowel alphabet"
        case 'i': return "vowel alphabet"
        case _ : return  "simple alphabet"
print(checkvowel('a')) 
print(checkvowel('m')) 
print(checkvowel('k'))     



words = ["one","two","three","kuchi"]
for x in words:
    print(x)

i=2
while i<30:
    print(i)
    i +=2

x=0
while x < 10:
  print("x",x)
if x==5:
    print("breaking...")
    break
x+=1
print(end)




