# importing time library for time code below

import datetime


# dictionary has username(s) and password(s)

users = {'ahmet': 'sehir123', 'meryem': '4444', 'a': 'a'}  # ad, sifre


inventory={'asparagus':[10,5],'broccoli':[15,6],'carrots':[18,7],'apples':[20,5],'banana':[10,8],'berries':[30,3],'eggs':[50,2],'mixed fruit juice':[0,8],'fish sticks':[25,12],'ice cream':[32,6], 'apple juice':[40,7], 'orange juice':[30,8],'grape juice':[10,9]}

splitted_inventory = {}
for i in inventory.keys():
    splitted_inv_list = i.split()
    splitted_inventory[i] = splitted_inv_list

baskets={}
basket=[]

main_menu = {1: 'Search for a product', 2: 'See Basket', 3: 'Check Out', 4: 'Logout', 5: 'Exit'}
basket_sub_menu = {1: 'Update amount', 2: 'Remove an item', 3: 'Check out', 4: 'Go back to main menu'}

def login():  # function to be used in log in action

    # making the codes which are going to use later in other functions 'global'

    global username

    print 'Please log in by providing your user credentials:'

    # asking user to enter username and password

    username = raw_input("User Name: ")
    password = raw_input("Password: ")

    if username in users and password == users[username]:  # checking if entered username is exist 'and' entered password matches with the right one
        print 'Successfully logged in!'
        print 'Welcome, ' + username + '! Please choose one of the following options by entering the corresponding menu number.'  # greeting


        menu()    #running menu function

    else:    #when username and/or password is not correct, runs login function again
        print 'Your user name and/or password is not correct. Please try again!'
        login()

def item_search(product):
    n = 1
    global k
    k = {}
    f = 0
    for i in splitted_inventory:
        if product in splitted_inventory[i]:
            k[n] = i
            print str(n) + '.', i, ' $' + str(inventory[i][1])
            n += 1
        elif product not in splitted_inventory[i]:
            f += 1


        if f == len(splitted_inventory):
            product = raw_input('Your search did not match any items. Please try something else (Enter 0 for main menu):')
            item_search(product)

def menu_1():
    product = raw_input("What are you searching for?")
    item_search(product)

    islem1 = int(raw_input('Please select which item you want to add to your basket (Enter 0 for main menu):'))
    if islem1 == 0:
        menu()
    else:
        amount = int(raw_input('Adding apple juice. Enter Amount:'))
        if amount > inventory[k[islem1]][0]:
            print 'Sorry! The amount exceeds the limit, Please try again with smaller amount'
            amount2 = raw_input('Amount (Enter 0 for main menu):')
            if int(amount2) == 0:
                menu()
            else:
                basket.append((k[islem1], amount))
                print 'Added apple juice into your Basket.\nGoing back to main menu...'
                baskets[username] = basket
                menu()

        else:
            basket.append((k[islem1], amount))
            print 'Added apple juice into your Basket.\nGoing back to main menu...'
            baskets[username] = basket
            menu()

#inventory={'asparagus':[10,5],'broccoli':[15,6],'carrots':[18,7],'apples':[20,5],'banana':[10,8],'berries':[30,3],'eggs':[50,2],'mixed fruit juice':[0,8],'fish sticks':[25,12],'ice cream':[32,6], 'apple juice':[40,7], 'orange juice':[30,8],'grape juice':[10,9]}

def checkout():
    print 'Processing your receipt...'
    print '******* Sehir Online Market ********\n************************************'
    print '44 44 0 34\nsehir.edu.tr'
    print '------------------------------------'
    tot = 0
    r = 1
    for i in baskets[username]:
        print str(r) + '.', i[0], 'price$=' + str(inventory[i[0]][1]), 'amount=' + str(i[1]), 'total=$' + str(
            (inventory[i[0]][1]) * (i[1]))
        inventory[i[0]][0]-= i[1]   #updating amount in inventory
        tot += (inventory[i[0]][1]) * (i[1])
    print '------------------------------------'
    print 'Total $'+ str(tot)
    print '------------------------------------'
    print datetime.datetime.now()
    print 'Thank You for using our Market!'
    menu()

def basket_menu_1():
    print 'Please choose an option:'
    for f in basket_sub_menu:
        print str(f) + '.' + basket_sub_menu[f]
    islem2=int(raw_input('Your selection:'))

    if islem2 == 1:
        None

    elif islem2 == 3:
        checkout()

    elif islem2 == 4:
        menu()


def menu():

    inventory = {'asparagus': [10, 5], 'broccoli': [15, 6], 'carrots': [18, 7], 'apples': [20, 5], 'banana': [10, 8], 'berries': [30, 3], 'eggs': [50, 2], 'mixed fruit juice': [0, 8], 'fish sticks': [25, 12], 'ice cream': [32, 6], 'apple juice': [40, 7], 'orange juice': [30, 8], 'grape juice': [10, 9]}

    # prints the keys and values of main_menu dictionary to show menu
    for i in main_menu:
        print str(i) + '. ' + main_menu[i]

    islem0 = raw_input("Please choose one of the following Services:")    #asking for what user want in menu

    if int(islem0) > len(main_menu):    #if the given number greater than our last number show error
        print str(islem0) + ' is not a valid entry. Please choose from the above menu.'  #what user see when he/she write invalid number
        menu()#running the menu function

    # 1
    if int(islem0) == 1:  # if the given number is 1, then it's works
        menu_1()

    #baskets = {ahmet: [aspagus, 2], [orange juice, 3]}

    #inventory = {'asparagus': [10, 5], 'broccoli': [15, 6], 'carrots': [18, 7], 'apples': [20, 5], 'banana': [10, 8],
    #             'berries': [30, 3], 'eggs': [50, 2], 'mixed fruit juice': [0, 8], 'fish sticks': [25, 12],
    #             'ice cream': [32, 6], 'apple juice': [40, 7], 'orange juice': [30, 8], 'grape juice': [10, 9]}

    #2
    elif int(islem0) == 2:
        r=1
        tot = 0
        try:
            print 'Your basket contains:'
            for i in baskets[username]:
                print str(r)+'.', i[0], 'price$='+str(inventory[i[0]][1]), 'amount='+str(i[1]), 'total=$'+str((inventory[i[0]][1])*(i[1]))
                tot+=(inventory[i[0]][1])*(i[1])
                r+=1
            print 'Total $'+str(tot)
            basket_menu_1()
        except KeyError:
            print 'Your basket is empty\nTotal price= $0'
            basket_menu_1()
    #3
    elif int(islem0) == 3:
        checkout()

    # 4
    elif int(islem0) == 4:  #if the given number is 4, then it's works
        main()

    # 5
    elif int(islem0) == 5:#if the entry is 5, program terminates it self
        print 'Program Terminated !'

def main():
    print "****Welcome to Sehir Online Market****"
    login()

main()