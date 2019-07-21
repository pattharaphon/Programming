#!/usr/bin/env python
# coding: utf-8

# In[6]:


Usernameinput = input("Username :")
Passwordinput = input("Password:")
if Usernameinput=="Pattharaphon" and Passwordinput=="258369":
    print("Wecome To Pattharaphon Coffee")
    print("What do want to buy something?")
    print("This isall Menu in Pattharaphon Coffee")
    print("******************************")
    print("1.ชานมไข่มุก         35 THB")
    print("2.ชานมโกโก้         40 THB")
    print("3.แดงมะนาวโซดา  25 THB")
    print("4.เอสเพรสโซ่        45 THB")
    print("******************************")
    Cargo=int(input("Do you want to buy?"))
    
    if Cargo==1:
        value1=35
        print("Your Cargo:",Cargo," = ",value1,"THB")
    elif Cargo==2:
        value1=40
        print("Your Cargo:",Cargo," = ",value1,"THB")
    elif Cargo==3:
        value1=25
        print("Your Cargo:",Cargo," = ",value1,"THB")
    elif Cargo==4:
        value1=45
        print("Your Cargo:",Cargo," = ",value1,"THB")
    Qty1 =int(input("Do you want to Qty?"))
    
    if Cargo==1:
        value1=35
        print("Total:",Cargo," = ",value1*Qty1,"THB")
    elif Cargo==2:
        value1=40
        print("Total:",Cargo," = ",value1*Qty1,"THB")
    elif Cargo==3:
        value1=25
        print("Total:",Cargo," = ",value1*Qty1,"THB")
    elif Cargo==4:
        value1=45
        print("Total:",Cargo," = ",value1*Qty1,"THB")
    Cargo=int(input("Do you want to buy?"))
    
    if Cargo==1:
        value2=35
        print("Your Cargo:",Cargo," = ",value2,"THB")
    elif Cargo==2:
        value2=40
        print("Your Cargo:",Cargo," = ",value2,"THB")
    elif Cargo==3:
        value2=25
        print("Your Cargo:",Cargo," = ",value2,"THB")
    elif Cargo==4:
        value2=45
        print("Your Cargo:",Cargo," = ",value2,"THB")
    Qty2 =int(input("Do you want to Qty?"))
    
    if Cargo==1:
        cost2=35
        print("Total:",Cargo," = ",value2*Qty2,"THB")
    elif Cargo==2:
        cost2=40
        print("Total:",Cargo," = ",value2*Qty2,"THB")
    elif Cargo==3:
        cost2=25
        print("Total:",Cargo," = ",value2*Qty2,"THB")
    elif Cargo==4:
        cost2=45
        print("Total:",Cargo," = ",value2*Qty2,"THB")
    print("All Totall=",value1*Qty1+value2*Qty2,"THB")
else:
    print("ERROR")


# In[ ]:




