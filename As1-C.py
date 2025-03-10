'''Write a program that create a dictionary with the frequency of the
vowels from an inputted string. For example: input:’institute’.
Output:{‘i’:2,’u’:1,’e’:1} '''

class frquency():
    def __init__(self):
        self.str=str
        print("Enter a String to count the vowels :")
    def countVowels(self):
        v="aeiouAEIOU"
        c=0
        for i in self.str:
            if i in v:
                c+=1
        print("Number of vowels in the string is : ",c)
        count={i:self.str.count(i) for i in v if i in self.str}
        print(count)
a=frquency()
a.str=input()
a.countVowels()