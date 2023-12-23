name=input("Enter the name: ")
family=input("Enter the family: ")
mathmark=int(input("Enter your Math mark: "))
PEmark=int(input("Enter your P.E mark: "))
historymark=int(input("Enter your History mark: "))
Chemistmark=int(input("Enter your Chemist mark: "))
AVG=(Chemistmark+historymark+PEmark+mathmark)/4
print("Ms/Mr" , name, family,"your AVG is:",AVG)
