class student():
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
    def showdata(self):
        print("Student Name :",self.name,", Roll :",self.roll)
    def showmarks(self,marks):
        self.marks=marks
        print("The marks of the Student :",self.marks)
Sname=input("Enter your name :")
Sroll=int(input("Enter Student roll :"))
s1=student(Sname,Sroll)
s1.showdata()
mk=list(map(int,(input("Enter marks seperated by space :").split())))
s1.showmarks(mk)
sum=0
for val in mk:
    sum=sum+val
print("Total marks of Student :",sum)