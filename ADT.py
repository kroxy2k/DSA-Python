'''Create an ADT of array using OOPs concept.
Define a class with the name 𝑎𝑟𝑟𝑎𝑦1 and with the following members
Data member List 𝑙
Data member Size of the array 𝑚𝑎𝑥
Define a member function(constructor) __𝑖𝑛𝑖𝑡__ () which define an empty list 𝑙
and define size of the list.
Define member function 𝐶𝑟𝑒𝑎𝑡𝑒𝐴𝑟𝑟𝑎𝑦(), take input for the list 𝑙 with size 𝑚𝑎𝑥
Define member function 𝑆ℎ𝑜𝑤𝐴𝑟𝑟𝑎𝑦() display all the values of the array
Define member function 𝐿𝑖𝑛𝑒𝑎𝑟𝑆𝑒𝑎𝑟𝑐ℎ(), search one item in the array, return
index of the item
Define member function 𝑆𝑜𝑟𝑡𝑖𝑛𝑔(), arrange all the elements in sorted order
Define member function 𝐵𝑖𝑛𝑎𝑟𝑦𝑆𝑒𝑎𝑟𝑐ℎ(), return index of the item in the
sorted array
Write a main function, create an object of the class 𝑎𝑟𝑟𝑎𝑦1, call all the
member functions of the class 𝑎𝑟𝑟𝑎𝑦1 and implements data structure
operations on array.'''

class array1:
    def __init__(self, arr_max):
        self.l = []
        self.arr_max = arr_max
    
    def CreateArray(self):
        print(f"Enter {self.arr_max} elements:")
        for i in range(self.arr_max):
            element = int(input(f"Enter element {i + 1}: "))
            self.l.append(element)
    
    def ShowArray(self):
        print("Array elements:", self.l)

    def LinearSearch(self, key):
        for i in range(len(self.l)):
            if self.l[i] == key:
                return i  
        return -1  
    
    def Sorting(self):
        n = len(self.l)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if self.l[j] > self.l[j + 1]:  
                    self.l[j], self.l[j + 1] = self.l[j + 1], self.l[j]
        print("Sorted array:", self.l)


    def BinarySearch(self, key):
        low, high = 0, len(self.l) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.l[mid] == key:
                return mid  
            elif self.l[mid] < key:
                low = mid + 1
            else:
                high = mid - 1
        return -1  


if __name__ == "__main__":
    arr_max = int(input("Enter max size of array: "))
    ob = array1(arr_max)
    ob.CreateArray()
    ob.ShowArray()
    key = int(input("Enter element to search (Linear Search): "))
    result = ob.LinearSearch(key)
    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found")
    ob.Sorting()
    key = int(input("Enter element to search (Binary Search): "))
    result = ob.BinarySearch(key)
    if result != -1:
        print(f"Element found at index {result} after sorting")
    else:
        print("Element not found in sorted array")

