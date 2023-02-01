# Caiya Mimms | Jan 28,2023
# Sales_Tax_Program | HW #2.6
# Calculates Final Price of product including sles tax (User Input)

#Welcome text 
print("Howdy! This program will calutate sales tax for you!")
    
    #INPUTS(S) 

    #Getting purchase amount
per_a = float(input("Please enter the amount of your purchase (in dollars): "))
    
    #NO MAGIC NUMBERS!!
sta_tax_p = .05

cou_tax_p = .025

    # Calulating  State and County tax
sta_s_tax = per_a * sta_tax_p

con_s_tax = per_a * cou_tax_p

    #Adding both taxs to get total tax 
s_tax_total = sta_s_tax + con_s_tax
    
    #Calulateing Final/Total of the sale
total_s = per_a + s_tax_total

    #Outputs (5 reqired)

print("Your Purchase amount: ",per_a)
print("State sales tax: ",sta_s_tax)
print("County sales tax: ",con_s_tax)
print("Total sales tax: ",s_tax_total)
print("Total of the sale: ",total_s)

print("Program End")