class multiplefunctions():
    def subfields():
        print("Sub-fields in AI are:")
        lists=['machine learning','neural networks','vision','robotics','speech processing','natural language processing']
        for temp in lists:
            print(temp)
            
    def percentage():
        S1=int(input("Subject1:"))
        S2=int(input("Subject2:"))
        S3=int(input("Subject3:"))
        S4=int(input("Subject4:"))
        S5=int(input("Subject5:"))
        Total=S1+S2+S3+S4+S5
        print("Total:",S1+S2+S3+S4+S5)
        percentage=(Total/500)*100
        print("Percentage:",percentage)
        
    def OddEven():
        num=int(input("Enter a number:"))
        if((num%2)==0):
            print(num,"is Even number")
            message="Even number"
        else:
            print(num,"is Odd number")
 
    def Elegible():
        gender=input("Your Gender:")
        age=int(input("Your Age:"))
        if(gender=='male'):
            if(age>=21):
                print("ELEGIBLE")
                message="Elegible"
            else:
                print("NOT ELEGIBLE")
                message="Not Elegible"
        elif(gender=="female"):
            if(age>=18):
                print("ELEGIBLE")
                message="Elegible"
            else:
                print("NOT ELEGIBLE")
                meggage="Not Elegible"
            return message
 
    def triangle():
        Height=int(input("Height:"))
        breadth=int(input("Breadth:"))
        print("Area formula:(Height*Breadth)/2")
        Area=((Height*breadth)/2)
        print("Area of Triangle:",Area)
        Height1=int(input("Height1:"))
        Height2=int(input("Height2:"))
        Breadth=int(input("Breadth:"))
        print("Perimeter formula:Height1+Height2+Breadth")
        Perimeter=(Height1+Height2+Breadth)
        print("Perimeter of Triangle:",Perimeter)
        return Area,Perimeter       