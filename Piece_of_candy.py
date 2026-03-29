

response="no"
count=0
while response=="no":
 if count <3:
  response=input("May I have a piece of candy? ").lower()
 else:
  response=input("Please! I want it! ").lower()
 if response !="yes":
  response="no"
  count=count+1
print("Thank you")
