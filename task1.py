no=int(input("Enter any no :---"))
for row in range(1,no+1):
    a=("{}".format(row)*row)
    print(("*".join(a)),"=",row**row)