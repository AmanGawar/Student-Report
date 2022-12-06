repository={1234567894:"Aman",7654321982:"Prem",4567891230:"digu",1472583696:"Aman1",3261594871:"Prem1",9867534210:"digu1"}
c=list(repository.keys())
c1=[]
for i in repository:
    c1.append(repository[i])
repository1=dict(zip(c1,c))
name=input("Enter name: ")
def call3(name):
    print(repository1[name])
call3(name)


def call2(n):
    print(repository[n])
n=int(input("Enter contact number: "))
call2(n)
def call1(n1=len(c)):
    print("contact\t\tname")
    for j in range(n1):

       print(c[j],"\t\t",repository[c[j]])

a=input("Enter True if you want to extract whole data of repository: ")
if a=="True":
    call1()
a1=input("Enter True if you want to extract no of data: ")
if a1=="True":
    
  n1=int(input("Enter number of contact: "))
  call1(n1)
