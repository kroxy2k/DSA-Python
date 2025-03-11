'''Write a function thant takes a list of integers as a parameters and
returns third smallest number from the list. For example,
input:[34,89,54,20,50,76,10,45,90] output: 34'''

def trd_sml(n):
    for i in range(0,3):
        sml_indx=i
        for j in range(i+1,len(n)):
            if n[sml_indx]>n[j]:
                sml_indx=j
        n[i],n[sml_indx]=n[sml_indx],n[i]
    return n[2]


n = [10,20,30,40,50]
print(trd_sml(n))