from tkinter import *
import random
import time

#Functions

def receipt():
  textReceipt.delete(1.0,END)
  x=random.randint(100,1000)
  billnumber='BILL'+str(x)
  date=time.strftime('%d/%m/%Y')
  textReceipt.insert(END,'Receipt Ref:\t\t'+billnumber+'\t\t'+date+'\n')
  textReceipt.insert(END,'***************************************************************\n')
  textReceipt.insert(END,'Items :\t\t Cost of Items(Rs)\n')
  textReceipt.insert(END,'***************************************************************\n')
  if e_roll.get()!='0':
    textReceipt.insert(END,f'Roll\t\t\t{int(e_roll.get())*60}\n\n')
  if e_roti.get()!='0':
    textReceipt.insert(END,f'Roti\t\t\t{int(e_roti.get())*60}\n\n')
  if e_burger.get()!='0':
    textReceipt.insert(END,f'Burger\t\t\t{int(e_burger.get())*60}\n\n')
  if e_chowmein.get()!='0':
    textReceipt.insert(END,f'Chowmein\t\t\t{int(e_roll.get())*60}\n\n')
  if e_samosa.get()!='0':
    textReceipt.insert(END,f'Samosa\t\t\t{int(e_roll.get())*60}\n\n')
  if e_patties.get()!='0':
    textReceipt.insert(END,f'Patties\t\t\t{int(e_roll.get())*60}\n\n')
  if e_kachori.get()!='0':
    textReceipt.insert(END,f'Kachori\t\t\t{int(e_roll.get())*60}\n\n')
  if e_frenchfries.get()!='0':
    textReceipt.insert(END,f'French Fries\t\t\t{int(e_roll.get())*60}\n\n') 
  if e_pizza.get()!='0':
    textReceipt.insert(END,f'Pizza\t\t\t{int(e_roll.get())*60}\n\n')


  if e_tea.get()!='0':
    textReceipt.insert(END,f'Tea\t\t\t{int(e_roll.get())*60}\n\n')  
  if e_lassi.get()!='0':
    textReceipt.insert(END,f'Lassi\t\t\t{int(e_roll.get())*60}\n\n')
  if e_Cocacola.get()!='0':
    textReceipt.insert(END,f'Coca Cola\t\t\t{int(e_roll.get())*60}\n\n')
  if e_faluda.get()!='0':
    textReceipt.insert(END,f'Faluda\t\t\t{int(e_roll.get())*60}\n\n')
  if e_shikanji.get()!='0':
    textReceipt.insert(END,f'Shikanji\t\t\t{int(e_roll.get())*60}\n\n')
  if e_mountainDew.get()!='0':
    textReceipt.insert(END,f'Mountain Dew\t\t\t{int(e_roll.get())*60}\n\n')
  if e_jaljheera.get()!='0':
    textReceipt.insert(END,f'Jal Jheera\t\t\t{int(e_roll.get())*60}\n\n')
  if e_roohafza.get()!='0':
    textReceipt.insert(END,f'Roohafza\t\t\t{int(e_roll.get())*60}\n\n')   
  if e_masalatea.get()!='0':
    textReceipt.insert(END,f'Masala Tea\t\t\t{int(e_roll.get())*60}\n\n')  

  
  if e_plum.get()!='0':
    textReceipt.insert(END,f'Plum Cake\t\t\t{int(e_roll.get())*60}\n\n')
  if e_blackforest.get()!='0':
    textReceipt.insert(END,f'Blackforest Cake\t\t\t{int(e_roll.get())*60}\n\n')
  if e_vanilla.get()!='0':
    textReceipt.insert(END,f'Vanilla Cake\t\t\t{int(e_roll.get())*60}\n\n')
  if e_chocolate.get()!='0':
    textReceipt.insert(END,f'Chocolate Cake\t\t\t{int(e_roll.get())*60}\n\n')
  if e_oreocake.get()!='0':
    textReceipt.insert(END,f'Oreo Cake\t\t\t{int(e_roll.get())*60}\n\n')
  if e_strawberry.get()!='0':
    textReceipt.insert(END,f'Strawberry\t\t\t{int(e_roll.get())*60}\n\n')
  if e_brownie.get()!='0':
    textReceipt.insert(END,f'Brownie\t\t\t{int(e_roll.get())*60}\n\n')
  if e_redvelvet.get()!='0':
    textReceipt.insert(END,f'Red Velvet Cake\t\t\t{int(e_roll.get())*60}\n\n')
  if e_hazel.get()!='0':
    textReceipt.insert(END,f'Hazelnut Cake \t\t\t{int(e_roll.get())*60}\n\n')
  
  textReceipt.insert(END,'************************************************\n')
  if costoffoodvar.get()!='0 Rs':
    textReceipt.insert(END,f'Cost Of Food\t\t\t{priceofFood}Rs\n\n')
  if costofdrinkvar.get()!='0 Rs':
    textReceipt.insert(END,f'Cost Of Drinks\t\t\t{priceofDrinks}Rs\n\n')
  if costoffoodvar.get()!='0 Rs':
    textReceipt.insert(END,f'Cost Of Cakes\t\t\t{priceofCakes}Rs\n\n')

  textReceipt.insert(END,f'Sub Total\t\t\t{subtotalofItems}Rs\n\n')
  textReceipt.insert(END,f'Service Tax\t\t\t50 Rs\n\n')
  textReceipt.insert(END,f'Total Cost\t\t\t{totalcost}Rs\n\n')
  





def totalcost():
  global priceofFood,priceofDrinks,priceofCakes,subtotalofItems,totalcost,servicetaxvar
  item1=int(e_roll.get())
  item2=int(e_roti.get())
  item3=int(e_burger.get())
  item4=int(e_chowmein.get())
  item5=int(e_samosa.get())
  item6=int(e_patties.get())
  item7=int(e_kachori.get())
  item8=int(e_frenchfries.get())
  item9=int(e_pizza.get())


  item10=int(e_tea.get())
  item11=int(e_lassi.get())
  item12=int(e_Cocacola.get())
  item13=int(e_faluda.get())
  item14=int(e_shikanji.get())
  item15=int(e_mountainDew.get())
  item16=int(e_jaljheera.get())
  item17=int(e_roohafza.get())
  item18=int(e_masalatea.get())
  
  
  
  item19=int(e_plum.get())
  item20=int(e_blackforest.get())
  item21=int(e_vanilla.get())
  item22=int(e_chocolate.get())
  item23=int(e_oreocake.get())
  item24=int(e_strawberry.get())
  item25=int(e_brownie.get())
  item26=int(e_redvelvet.get())
  item27=int(e_hazel.get())

  priceofFood=(item1*10)+(item2*60)+(item3*45)+(item4*60)+(item5*120)+(item6*30)+(item7*120)+(item8*100)+(item9*120)

  priceofDrinks=(item10*15)+(item11*20)+(item12*30)+(item13*40)+(item14*25)+(item15*50)+(item16*35)+(item17*10)+(item18*20)

  priceofCakes=(item19*200)+(item20*300)+(item21*350)+(item22*300)+(item23*340)+(item24*450)+(item25*400)+(item26*300)+(item27*400)

  costoffoodvar.set(str(priceofFood)+'Rs')
  costofdrinkvar.set(str(priceofDrinks)+'Rs')
  costofcakevar.set(str(priceofCakes)+'Rs')

  subtotalofItems=priceofFood+priceofDrinks+priceofCakes
  subtotalvar.set(str(subtotalofItems)+'Rs')

  servicetaxvar.set('50 Rs')

  totalcost=subtotalofItems+50
  totalcostvar.set(str(totalcost)+'Rs')


def roll():
  if var1.get()==1:
    textroot1.config(state=NORMAL)
    textroot1.delete(0,END)
    textroot1.focus()
  else:
    textroot1.config(state=DISABLED)
    e_roll.set('0')

def roti():
  if var2.get()==1:
    textroot2.config(state=NORMAL)
    textroot2.delete(0,END)
    textroot2.focus()
  else:
    textroot2.config(state=DISABLED)
    e_roti.set('0')

def burger():
  if var3.get()==1:
    textroot3.config(state=NORMAL)
    textroot3.delete(0,END)
    textroot3.focus()
  else:
    textroot3.config(state=DISABLED)
    e_burger.set('0')

def chowmein():
  if var4.get()==1:
    textroot4.config(state=NORMAL)
    textroot4.delete(0,END)
    textroot4.focus()
  else:
    textroot4.config(state=DISABLED)
    e_chowmein.set('0')

def samosa():
  if var5.get()==1:
    textroot5.config(state=NORMAL)
    textroot5.delete(0,END)
    textroot5.focus()
  else:
    textroot5.config(state=DISABLED)
    e_samosa.set('0')

def patties():
  if var6.get()==1:
    textroot6.config(state=NORMAL)
    textroot6.delete(0,END)
    textroot6.focus()
  else:
    textroot6.config(state=DISABLED)
    e_patties.set('0')

def kachori():
  if var7.get()==1:
    textroot7.config(state=NORMAL)
    textroot7.delete(0,END)
    textroot7.focus()
  else:
    textroot7.config(state=DISABLED)
    e_kachori.set('0')

def frenchfries():
  if var8.get()==1:
    textroot8.config(state=NORMAL)
    textroot8.delete(0,END)
    textroot8.focus()
  else:
    textroot8.config(state=DISABLED)
    e_frenchfries.set('0')

def pizza():
  if var99.get()==1:
    textroot9.config(state=NORMAL)
    textroot9.delete(0,END)
    textroot9.focus()
  else:
    textroot9.config(state=DISABLED)
    e_pizza.set('0')

def tea():
  if var9.get()==1:
    textdrink1.config(state=NORMAL)
    textdrink1.delete(0,END)
    textdrink1.focus()
  else:
    textdrink1.config(state=DISABLED)
    e_tea.set('0')

def lassi():
  if var10.get()==1:
    textdrink2.config(state=NORMAL)
    textdrink2.delete(0,END)
    textdrink2.focus()
  else:
    textdrink2.config(state=DISABLED)
    e_lassi.set('0')

def Cocacola():
  if var11.get()==1:
    textdrink3.config(state=NORMAL)
    textdrink3.delete(0,END)
    textdrink3.focus()
  else:
    textdrink3.config(state=DISABLED)
    e_Cocacola.set('0')

def faluda():
  if var12.get()==1:
    textdrink4.config(state=NORMAL)
    textdrink4.delete(0,END)
    textdrink4.focus()
  else:
    textdrink4.config(state=DISABLED)
    e_faluda.set('0')

def shikanji():
  if var13.get()==1:
    textdrink5.config(state=NORMAL)
    textdrink5.delete(0,END)
    textdrink5.focus()
  else:
    textdrink5.config(state=DISABLED)
    e_shikanji.set('0')

def mountainDew():
  if var14.get()==1:
    textdrink6.config(state=NORMAL)
    textdrink6.delete(0,END)
    textdrink6.focus()
  else:
    textdrink6.config(state=DISABLED)
    e_mountainDew.set('0')

def jaljheera():
  if var15.get()==1:
    textdrink7.config(state=NORMAL)
    textdrink7.delete(0,END)
    textdrink7.focus()
  else:
    textdrink7.config(state=DISABLED)
    e_jaljheera.set('0')

def roohafza():
  if var16.get()==1:
    textdrink8.config(state=NORMAL)
    textdrink8.delete(0,END)
    textdrink8.focus()
  else:
    textdrink8.config(state=DISABLED)
    e_roohafza.set('0')

def masalatea():
  if var17.get()==1:
    textdrink9.config(state=NORMAL)
    textdrink9.delete(0,END)
    textdrink9.focus()
  else:
    textdrink9.config(state=DISABLED)
    e_masalatea.set('0')

def plum():
  if var18.get()==1:
    textcake1.config(state=NORMAL)
    textcake1.delete(0,END)
    textcake1.focus()
  else:
    textcake1.config(state=DISABLED)
    e_plum.set('0')

def blackforest():
  if var19.get()==1:
    textcake2.config(state=NORMAL)
    textcake2.delete(0,END)
    textcake2.focus()
  else:
    textcake2.config(state=DISABLED)
    e_blackforest.set('0')

def vanilla():
  if var20.get()==1:
    textcake3.config(state=NORMAL)
    textcake3.delete(0,END)
    textcake3.focus()
  else:
    textcake3.config(state=DISABLED)
    e_vanilla.set('0')

def chocolate():
  if var21.get()==1:
    textcake4.config(state=NORMAL)
    textcake4.delete(0,END)
    textcake4.focus()
  else:
    textcake4.config(state=DISABLED)
    e_chocolate.set('0')

def oreocake():
  if var22.get()==1:
    textcake5.config(state=NORMAL)
    textcake5.delete(0,END)
    textcake5.focus()
  else:
    textcake5.config(state=DISABLED)
    e_oreocake.set('0')

def strawberry():
  if var23.get()==1:
    textcake6.config(state=NORMAL)
    textcake6.delete(0,END)
    textcake6.focus()
  else:
    textcake6.config(state=DISABLED)
    e_strawberry.set('0')

def brownie():
  if var24.get()==1:
    textcake7.config(state=NORMAL)
    textcake7.delete(0,END)
    textcake7.focus()
  else:
    textcake7.config(state=DISABLED)
    e_brownie.set('0')

def redvelvet():
  if var25.get()==1:
    textcake8.config(state=NORMAL)
    textcake8.delete(0,END)
    textcake8.focus()
  else:
    textcake8.config(state=DISABLED)
    e_redvelvet.set('0')

def hazel():
  if var26.get()==1:
    textcake9.config(state=NORMAL)
    textcake9.delete(0,END)
    textcake9.focus()
  else:
    textcake9.config(state=DISABLED)
    e_hazel.set('0')




root=Tk()
root.geometry('1370x699+0+0')
root.resizable(0,0)
root.title('Canteen Order System')
root.config(bg='firebrick4')
topFrame=Frame(root,bd=10,relief=RIDGE)
topFrame.pack(side=TOP)
labelTitle=Label(topFrame,text='Canteen Order System',font=('arial',30,'bold'),bg='firebrick4',fg='yellow')
labelTitle.grid(row=0,column=0)
#frames
menuFrame=Frame(root,bd=10,relief=RIDGE,bg='firebrick4')
menuFrame.pack(side=LEFT)

costFrame=Frame(menuFrame,bd=4,relief=RIDGE,bg='firebrick4')
costFrame.pack(side=BOTTOM)

foodFrame=LabelFrame(menuFrame,text='Food',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='red4')
foodFrame.pack(side=LEFT)

drinksFrame=LabelFrame(menuFrame,text='Drinks',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='red4')
drinksFrame.pack(side=LEFT)

cakesFrame=LabelFrame(menuFrame,text='Cakes',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='red4')
cakesFrame.pack(side=LEFT)

rightFrame=Frame(root,bd=15,relief=RIDGE,bg='red4')
rightFrame.pack(side=RIGHT)

calculatorFrame=Frame(rightFrame,bd=1,relief=RIDGE,bg='red4')
calculatorFrame.pack()

recieptFrame=Frame(rightFrame,bd=4,relief=RIDGE,bg='red4')
recieptFrame.pack()

buttonFrame=Frame(rightFrame,bd=3,relief=RIDGE,bg='red4')
buttonFrame.pack()

##VARIABLE
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var99=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
var17=IntVar()
var18=IntVar()
var19=IntVar()
var20=IntVar()
var21=IntVar()
var22=IntVar()
var23=IntVar()
var24=IntVar()
var25=IntVar()
var26=IntVar()


e_roll=StringVar()
e_roti=StringVar()
e_burger=StringVar()
e_chowmein=StringVar()
e_samosa=StringVar()
e_patties=StringVar()
e_kachori=StringVar()
e_frenchfries=StringVar()
e_pizza=StringVar()


e_tea=StringVar()
e_lassi=StringVar()
e_Cocacola=StringVar()
e_faluda=StringVar()
e_shikanji=StringVar()
e_mountainDew=StringVar()
e_jaljheera=StringVar()
e_roohafza=StringVar()
e_masalatea=StringVar()


e_plum=StringVar()
e_blackforest=StringVar()
e_vanilla=StringVar()
e_chocolate=StringVar()
e_oreocake=StringVar()
e_strawberry=StringVar()
e_brownie=StringVar()
e_redvelvet=StringVar()
e_hazel=StringVar()


costoffoodvar=StringVar()
costofdrinkvar=StringVar()
costofcakevar=StringVar()
subtotalvar=StringVar()
servicetaxvar=StringVar()
totalcostvar=StringVar()



e_roll.set(0)
e_roti.set(0)
e_burger.set(0)
e_chowmein.set(0)
e_samosa.set(0)
e_patties.set(0)
e_kachori.set(0)
e_frenchfries.set(0)
e_pizza.set(0)

e_tea.set(0)
e_lassi.set(0)
e_Cocacola.set(0)
e_faluda.set(0)
e_shikanji.set(0)
e_mountainDew.set(0)
e_jaljheera.set(0)
e_roohafza.set(0)
e_masalatea.set(0)


e_plum.set(0)
e_blackforest.set(0)
e_vanilla.set(0)
e_chocolate.set(0)
e_oreocake.set(0)
e_strawberry.set(0)
e_brownie.set(0)
e_redvelvet.set(0)
e_hazel.set(0)


##FOOD

roll=Checkbutton(foodFrame,text='Chowmein Roll',font=('arial',18,'bold'),onvalue=0,offvalue=1,variable=var1,command=roll)
roll.grid(row=0,column=0,sticky=W)

roti=Checkbutton(foodFrame,text='Roti Sabzi',font=('arial',18,'bold'),onvalue=0,offvalue=1,variable=var2,command=roti)
roti.grid(row=1,column=0,sticky=W)

burger=Checkbutton(foodFrame,text='Burger',font=('arial',18,'bold'),onvalue=0,offvalue=1,variable=var3,command=burger)
burger.grid(row=2,column=0,sticky=W)

chowmein=Checkbutton(foodFrame,text='Chowmein',font=('arial',18,'bold'),onvalue=0,offvalue=1,variable=var4,command=chowmein)
chowmein.grid(row=3,column=0,sticky=W)

samosa=Checkbutton(foodFrame,text='Samosa',font=('arial',18,'bold'),onvalue=0,offvalue=1,variable=var5,command=samosa)
samosa.grid(row=4,column=0,sticky=W)

patties=Checkbutton(foodFrame,text='Patties',font=('arial',18,'bold'),onvalue=0,offvalue=1,variable=var6,command=patties)
patties.grid(row=5,column=0,sticky=W)

kachori=Checkbutton(foodFrame,text='Kachori',font=('arial',18,'bold'),onvalue=0,offvalue=1,variable=var7,command=kachori)
kachori.grid(row=6,column=0,sticky=W)

frenchfries=Checkbutton(foodFrame,text='French Fries',font=('arial',18,'bold'),onvalue=0,offvalue=1,variable=var8,command=frenchfries)
frenchfries.grid(row=7,column=0,sticky=W)

pizza=Checkbutton(foodFrame,text='Pizza',font=('arial',18,'bold'),onvalue=0,offvalue=1,variable=var99,command=pizza)
pizza.grid(row=8,column=0,sticky=W)



#Entry Fields for food Items

textroot1=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=4,state=DISABLED,textvariable=e_roll)
textroot1.grid(row=0,column=1)

textroot2=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=4,state=DISABLED,textvariable=e_roti)
textroot2.grid(row=1,column=1)

textroot3=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=4,state=DISABLED,textvariable=e_burger)
textroot3.grid(row=2,column=1)

textroot4=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=4,state=DISABLED,textvariable=e_chowmein)
textroot4.grid(row=3,column=1)

textroot5=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=4,state=DISABLED,textvariable=e_samosa)
textroot5.grid(row=4,column=1)

textroot6=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=4,state=DISABLED,textvariable=e_patties)
textroot6.grid(row=5,column=1)

textroot7=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=4,state=DISABLED,textvariable=e_kachori)
textroot7.grid(row=6,column=1)

textroot8=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=4,state=DISABLED,textvariable=e_frenchfries)
textroot8.grid(row=7,column=1)

textroot9=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=4,state=DISABLED,textvariable=e_pizza)
textroot9.grid(row=8,column=1)


#Drinks

tea=Checkbutton(drinksFrame,text='Tea',font=('arial',18,'bold'),onvalue=0,offvalue=1,variable=var9,command=tea)
tea.grid(row=0,column=0,sticky=W)

lassi=Checkbutton(drinksFrame,text='Lassi',font=('arial',18,'bold'),onvalue=0,offvalue=1,variable=var10,command=lassi)
lassi.grid(row=1,column=0,sticky=W)

Cocacola=Checkbutton(drinksFrame,text='Coca Cola',font=('arial',18,'bold'),onvalue=0,offvalue=1,variable=var11,command=Cocacola)
Cocacola.grid(row=2,column=0,sticky=W)

faluda=Checkbutton(drinksFrame,text='Faluda',font=('arial',18,'bold'),onvalue=0,offvalue=1,variable=var12,command=faluda)
faluda.grid(row=3,column=0,sticky=W)

shikanji=Checkbutton(drinksFrame,text='Shikanji',font=('arial',18,'bold'),onvalue=0,offvalue=1,variable=var13,command=shikanji)
shikanji.grid(row=4,column=0,sticky=W)

mountainDew=Checkbutton(drinksFrame,text='Mountain Dew',font=('arial',18,'bold'),onvalue=0,offvalue=1,variable=var14,command=mountainDew)
mountainDew.grid(row=5,column=0,sticky=W)

jaljheera=Checkbutton(drinksFrame,text='Jal Jheera',font=('arial',18,'bold'),onvalue=0,offvalue=1,variable=var15,command=jaljheera)
jaljheera.grid(row=6,column=0,sticky=W)
 
roohafza=Checkbutton(drinksFrame,text='Roohafza',font=('arial',18,'bold'),onvalue=0,offvalue=1,variable=var16,command=roohafza)
roohafza.grid(row=7,column=0,sticky=W)

masalatea=Checkbutton(drinksFrame,text='Masala Tea',font=('arial',18,'bold'),onvalue=0,offvalue=1,variable=var17,command=masalatea)
masalatea.grid(row=8,column=0,sticky=W)

#Entry Fields for drinks

textdrink1=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=4,state=DISABLED,textvariable=e_tea)
textdrink1.grid(row=0,column=1)

textdrink2=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=4,state=DISABLED,textvariable=e_lassi)
textdrink2.grid(row=1,column=1)

textdrink3=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=4,state=DISABLED,textvariable=e_Cocacola)
textdrink3.grid(row=2,column=1)

textdrink4=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=4,state=DISABLED,textvariable=e_faluda)
textdrink4.grid(row=3,column=1)

textdrink5=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=4,state=DISABLED,textvariable=e_shikanji)
textdrink5.grid(row=4,column=1)

textdrink6=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=4,state=DISABLED,textvariable=e_mountainDew)
textdrink6.grid(row=5,column=1)

textdrink7=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=4,state=DISABLED,textvariable=e_jaljheera)
textdrink7.grid(row=6,column=1)

textdrink8=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=4,state=DISABLED,textvariable=e_roohafza)
textdrink8.grid(row=7,column=1)

textdrink9=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=4,state=DISABLED,textvariable=e_masalatea)
textdrink9.grid(row=8,column=1)

#Cakes

plum=Checkbutton(cakesFrame,text='Plum Cake',font=('arial',18,'bold'),onvalue=0,offvalue=1,variable=var18,command=plum)
plum.grid(row=0,column=0,sticky=W)

blackforest=Checkbutton(cakesFrame,text='Black Forest',font=('arial',18,'bold'),onvalue=0,offvalue=1,variable=var19,command=blackforest)
blackforest.grid(row=1,column=0,sticky=W)

vanilla=Checkbutton(cakesFrame,text='Vanilla',font=('arial',18,'bold'),onvalue=0,offvalue=1,variable=var20,command=vanilla)
vanilla.grid(row=2,column=0,sticky=W)

chocolate=Checkbutton(cakesFrame,text='Chocolate',font=('arial',18,'bold'),onvalue=0,offvalue=1,variable=var21,command=chocolate)
chocolate.grid(row=3,column=0,sticky=W)

oreocake=Checkbutton(cakesFrame,text='Oreo Cake',font=('arial',18,'bold'),onvalue=0,offvalue=1,variable=var22,command=oreocake)
oreocake.grid(row=4,column=0,sticky=W)

strawberry=Checkbutton(cakesFrame,text='Strawberry',font=('arial',18,'bold'),onvalue=0,offvalue=1,variable=var23,command=strawberry)
strawberry.grid(row=5,column=0,sticky=W)

brownie=Checkbutton(cakesFrame,text='Brownie',font=('arial',18,'bold'),onvalue=0,offvalue=1,variable=var24,command=brownie)
brownie.grid(row=6,column=0,sticky=W)

redvelvet=Checkbutton(cakesFrame,text='Red Velvet Cake',font=('arial',18,'bold'),onvalue=0,offvalue=1,variable=var25,command=redvelvet)
redvelvet.grid(row=7,column=0,sticky=W)

hazel=Checkbutton(cakesFrame,text='Hazelnut Cake',font=('arial',18,'bold'),onvalue=0,offvalue=1,variable=var26,command=hazel)
hazel.grid(row=8,column=0,sticky=W)


#Entry Fields for Cakes

textcake1=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=4,state=DISABLED,textvariable=e_plum)
textcake1.grid(row=0,column=1)

textcake2=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=4,state=DISABLED,textvariable=e_blackforest)
textcake2.grid(row=1,column=1)

textcake3=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=4,state=DISABLED,textvariable=e_vanilla)
textcake3.grid(row=2,column=1)

textcake4=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=4,state=DISABLED,textvariable=e_chocolate)
textcake4.grid(row=3,column=1)

textcake5=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=4,state=DISABLED,textvariable=e_oreocake)
textcake5.grid(row=4,column=1)

textcake6=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=4,state=DISABLED,textvariable=e_strawberry)
textcake6.grid(row=5,column=1)

textcake7=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=4,state=DISABLED,textvariable=e_brownie)
textcake7.grid(row=6,column=1)

textcake8=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=4,state=DISABLED,textvariable=e_redvelvet)
textcake8.grid(row=7,column=1)

textcake9=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=4,state=DISABLED,textvariable=e_hazel)
textcake9.grid(row=8,column=1)



#Cost Labels & Entry Fields

labelCostofFood=Label(costFrame,text='Cost Of Food Items',font=('arial',16,'bold'),fg='white',bg='firebrick4')
labelCostofFood.grid(row=0,column=0)

textCostofFood=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costoffoodvar)
textCostofFood.grid(row=0,column=1,padx=41,pady=5)

labelCostofDrinks=Label(costFrame,text='Cost Of Drinks',font=('arial',16,'bold'),fg='white',bg='firebrick4')
labelCostofDrinks.grid(row=1,column=0)

textCostofDrinks=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costofdrinkvar)
textCostofDrinks.grid(row=1,column=1,padx=41,pady=5)

labelCostofCakes=Label(costFrame,text='Cost Of Cakes',font=('arial',16,'bold'),fg='white',bg='firebrick4')
labelCostofCakes.grid(row=2,column=0)

textCostofCakes=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costofcakevar)
textCostofCakes.grid(row=2,column=1,padx=41,pady=5)

labelSubtotal=Label(costFrame,text='Sub Total',font=('arial',16,'bold'),fg='white',bg='firebrick4')
labelSubtotal.grid(row=0,column=2)

textSubtotal=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=subtotalvar)
textSubtotal.grid(row=0,column=3,padx=41,pady=5)

labelServiceTax=Label(costFrame,text='Service Tax',font=('arial',16,'bold'),fg='white',bg='firebrick4')
labelServiceTax.grid(row=1,column=2)

textServiceTax=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=servicetaxvar)
textServiceTax.grid(row=1,column=3,padx=41,pady=5)

 
labelTotalCost=Label(costFrame,text='Total Cost',font=('arial',16,'bold'),fg='white',bg='firebrick4')
labelTotalCost.grid(row=2,column=2)

textTotalCost=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=totalcostvar)
textTotalCost.grid(row=2,column=3,padx=41,pady=5)

#Buttons

buttonTotal=Button(buttonFrame,text='Total',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=5,command=totalcost)
buttonTotal.grid(row=0,column=0)

buttonReciept=Button(buttonFrame,text='Receipt',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=5,command=receipt)
buttonReciept.grid(row=0,column=1)
padx=41
buttonSave=Button(buttonFrame,text='Save',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=5)
buttonSave.grid(row=0,column=2)

buttonSend=Button(buttonFrame,text='Send',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=5)
buttonSend.grid(row=0,column=3)

buttonReset=Button(buttonFrame,text='Reset',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=5)
buttonReset.grid(row=0,column=4)


#textarea for Receipt

textReceipt=Text(recieptFrame,font=('arial',12,'bold'),bd=3,width=42,height=14,)
textReceipt.grid(row=0,column=0)

#Calculator

operator=''
def buttonClick(numbers):
  global operator
  operator=operator+numbers
  calculatorField.delete(0,END)
  calculatorField.insert(END,operator)

def clear():
  global operator
  operator=''
  calculatorField.delete(0,END)

def answer():
  global operator
  result=str(eval(operator))
  calculatorField.delete(0,END)
  calculatorField.insert(0,result)
  operator=''

calculatorField=Entry(calculatorFrame,font=('arial',16,'bold'),width=32,bd=4,state='normal')
calculatorField.grid(row=0,column=0,columnspan=4)

button7=Button(calculatorFrame,text='7',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('7'))
button7.grid(row=1,column=0)

button8=Button(calculatorFrame,text='8',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('8'))
button8.grid(row=1,column=1)

button9=Button(calculatorFrame,text='9',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('9'))
button9.grid(row=1,column=2)

buttonPlus=Button(calculatorFrame,text='+',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('+'))
buttonPlus.grid(row=1,column=3)

button4=Button(calculatorFrame,text='4',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('4'))
button4.grid(row=2,column=0)

button5=Button(calculatorFrame,text='5',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('5'))
button5.grid(row=2,column=1)

button6=Button(calculatorFrame,text='6',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('6'))
button6.grid(row=2,column=2)

buttonminus=Button(calculatorFrame,text='-',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('-'))
buttonminus.grid(row=2,column=3)

button3=Button(calculatorFrame,text='3',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('3'))
button3.grid(row=3,column=0)

button2=Button(calculatorFrame,text='2',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('2'))
button2.grid(row=3,column=1)

button1=Button(calculatorFrame,text='1',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('1'))
button1.grid(row=3,column=2)

buttonstar=Button(calculatorFrame,text='*',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('*'))
buttonstar.grid(row=3,column=3)

buttonans=Button(calculatorFrame,text='Ans',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=answer)
buttonans.grid(row=4,column=0)

buttonclear=Button(calculatorFrame,text='Clear',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=clear)
buttonclear.grid(row=4,column=1)

button0=Button(calculatorFrame,text='0',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('0'))
button0.grid(row=4,column=2)

buttonslash=Button(calculatorFrame,text='/',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('/'))
buttonslash.grid(row=4,column=3)



root.mainloop()



