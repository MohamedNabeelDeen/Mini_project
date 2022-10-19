"""Family banking system application developed by Mohamed Nabeel Deen - 40226125
        Using Vanilla Python and Built-in Libraries.

    Family Usernames :
        Dad and Mom : Brad and Ana
        Children : Catherine, david, Eon, Faz, helena, irene, Jackson
"""

import datetime, json,os,pickle,time
FIRST_TIME_FLAG = True

try:
    with open('Transaction_Instances.pkl', 'rb') as inp:
        Transaction_Instances = pickle.load(inp)

except Exception as e:
    print(e)
    Transaction_Instances = []
    Wallet_Instances = []
    Member_Instances = []
    Notifications_List = []


class Wallet:
    def __init__(self):
        self.balance = 0

    def deposit(self, member, amount, CURRENT_MEMBER):
        if CURRENT_MEMBER.isParent:
            if amount > 0:
                member.wallet.balance += amount
                print(amount, "$ Deposited to", member.name, "\n", "By ---------------- ", CURRENT_MEMBER.name)
        else:
            print("Not a parent")

    def withdraw(self, amount):
        if amount > 0:
            self.balance -= amount


class Transaction:
    def __init__(self, Family_Member, amount, retail_store, item_list):
        self.member = Family_Member
        self.timeStamp = datetime.datetime.now()
        self.amount = amount
        self.retail_store = retail_store
        self.item_list = item_list
        self.status = True
        Transaction_Instances.append(self)

        todays_transaction = []
        for tx in Transaction_Instances:
            if tx.member == Family_Member:

                if tx.timeStamp.date() == datetime.datetime.now().date():
                    todays_transaction.append(tx)

        if not Family_Member.isParent:
            if len(todays_transaction) >= 2:
                Notifications_List.append("{} Tried to do more than one transaction today".format(Family_Member.name))

        total_today = 0
        for tx_today in todays_transaction:
            total_today += tx_today.amount

        if total_today > 50:
            self.status = False

        if Family_Member.isBlocked:
            self.status = False
            print("You have been Blocked by Dad")

        if self.member.wallet.balance - self.amount < 0:
            self.status = False
            print("\nNot enough Balance")

        if self.status:
            print(
                "Purchase completed: Store Name-{} ,Item-{} ,Price-{} ".format(str(retail_store), str(item_list),
                                                                               str(amount)))
            self.member.wallet.withdraw(self.amount)

    @staticmethod
    def view_all_transactions(member):
        if member.isParent:
            print("Displaying all transactions.")
            print("----------------------------")
            for tx in Transaction_Instances:
                print("Date of Transaction: {}\nTransaction went through: {}\nRetail Store name: {}\nItems: {}\n"
                      "Done by: {}\nAmount: ${}\n----------------------------"
                      "".format(tx.timeStamp.date(), tx.status, tx.retail_store, tx.item_list, tx.member.name,
                                tx.amount))
        else:
            print("Not a parent")


class FamilyMember:
    def __init__(self, name, is_parent, is_dad, is_blocked):
        self.name = name
        self.isParent = is_parent
        self.isDad = is_dad
        self.isBlocked = is_blocked
        self.wallet = Wallet()
        Wallet_Instances.append(self.wallet)

    def block_member(dad, member):
        if dad.isDad:
            member.isBlocked = True
            print("{} blocked {}".format(dad.name, member.name))
        else:
            print("Not a Father")

    def unblock_member(dad, member):
        if dad.isDad:
            member.isBlocked = False
            print("{} unblocked {}".format(dad.name, member.name))
        else:
            print("Not a Father")


class Notification:
    def __init__(self, name, content):
        self.name = name
        self.content = content


try:
    with open('Wallet_Instances.pkl', 'rb') as inp:
        Wallet_Instances = pickle.load(inp)
    with open('Member_Instances.pkl', 'rb') as inp:
        Member_Instances = pickle.load(inp)
    with open('Notifications_List.pkl', 'rb') as inp:
        Notifications_List = pickle.load(inp)
except:
    pass

if FIRST_TIME_FLAG:
    # Family Member Creation
    json_family = json.load(open("family_members.json", "r"))
    for member in json_family:
        member_temp = FamilyMember(member["name"], member["isParent"], member["isDad"], member["isBlocked"])
        Member_Instances.append(member_temp)

if FIRST_TIME_FLAG:
    with open('Transaction_Instances.pkl', 'wb') as outp:
        pickle.dump(Transaction_Instances, outp, pickle.HIGHEST_PROTOCOL)
    with open('Wallet_Instances.pkl', 'wb') as outp:
        pickle.dump(Wallet_Instances, outp, pickle.HIGHEST_PROTOCOL)
    with open('Member_Instances.pkl', 'wb') as outp:
        pickle.dump(Member_Instances, outp, pickle.HIGHEST_PROTOCOL)
    with open('Notifications_List.pkl', 'wb') as outp:
        pickle.dump(Notifications_List, outp, pickle.HIGHEST_PROTOCOL)

# Transactions Array to store Transaction object creation
transactions = []
Father = Member_Instances[8]
Mother = Member_Instances[9]


def get_member_object(name):
    for fam_member in Member_Instances:
        if fam_member.name.lower() == name.lower():
            return fam_member
    return "Not A Member"


def refresh_data():
    with open('Transaction_Instances.pkl', 'wb') as outp:
        outp.truncate()
        pickle.dump(Transaction_Instances, outp, pickle.HIGHEST_PROTOCOL)
    with open('Wallet_Instances.pkl', 'wb') as outp:
        outp.truncate()
        pickle.dump(Wallet_Instances, outp, pickle.HIGHEST_PROTOCOL)
    with open('Member_Instances.pkl', 'wb') as outp:
        outp.truncate()
        pickle.dump(Member_Instances, outp, pickle.HIGHEST_PROTOCOL)
    with open('Notifications_List.pkl', 'wb') as outp:
        outp.truncate()
        pickle.dump(Notifications_List, outp, pickle.HIGHEST_PROTOCOL)


def notifications(member):
    if member.isParent:
        count = 0
        print("\n--------------NOTIFICATIONS-----------------\n")
        for member in Member_Instances:
            if member.wallet.balance < 100:
                print("{}'s Wallet is below 100$".format(Member_Instances[count].name))
            count += 1
            if count == 10:
                break
        print("-------------------------------------------------")
        for note in Notifications_List:
            print(note.content)
        print("-------------------------------------------------")
        for member in Member_Instances:
            if member.isBlocked:
                print(member.name + " Has been Blocked By Brad.")
    else:
        print("-------------------------------------------------")
        print("Only a Parent can access the Notifications")


def add_request(member):
    Notifications_List.append(Notification(name=member.name, content=member.name + " has a request"))
    # print(Notifications_List)


print("--------------------------------------------------------------------------------")
print("Bonjour!\n"
      "Welcome to the wallet\n")
username = input("Enter the Username:")

CURRENT_MEMBER = 0
for fam_member in Member_Instances:
    if fam_member.name.lower() == username.lower():
        CURRENT_MEMBER = fam_member
        break
if not CURRENT_MEMBER:
    print("Incorrect UserName, Please login again")


def main_menu():
    # Refreshes the Data States of the program.
    refresh_data()
    print("-------------------------------------------------\n")

    print("Welcome: {}                  ".format(CURRENT_MEMBER.name) + str(datetime.datetime.now()) + "\n")
    if CURRENT_MEMBER.isParent:

        print("1-DEPOSIT      2-PURCHASE        3-VIEW TRANSACTIONS        4-VIEW BALANCE      5-NOTIFICATION\n")
        print("               6-BLOCK           7-UNBLOCK                  8-LOGOUT \n")
        select_mode = int(input("Enter your Choice: "))

        if select_mode == 1:
            amount = int(input("Enter the amount to be deposited"))
            name = input("Enter the name of the recipient")
            member = get_member_object(name)
            member.wallet.deposit(member, amount, CURRENT_MEMBER)
            main_menu()
        elif select_mode == 2:
            print("Enter the item, price and store:")
            item = input()
            price = int(input().split("$")[0])
            store_name = input()
            transactions.append(Transaction(CURRENT_MEMBER, price, store_name, item))
            main_menu()

        elif select_mode == 3:
            Transaction.view_all_transactions(CURRENT_MEMBER)
            main_menu()

        elif select_mode == 4:
            print("Your Current Balance is", str(CURRENT_MEMBER.wallet.balance) + "$")
            main_menu()

        elif select_mode == 5:
            notifications(CURRENT_MEMBER)
            main_menu()

        elif select_mode == 6:
            usernamme = input("Enter the User to be Blocked:")
            if usernamme == "Not A Member":
                print("Invalid username, going back to the menu")
                main_menu()
            user = get_member_object(usernamme)
            FamilyMember.block_member(CURRENT_MEMBER, user)
            main_menu()

        elif select_mode == 7:
            usernamme = input("Enter the User to be UnBlocked:")
            if usernamme == "Not A Member":
                print("Invalid username, going back to the menu")
                main_menu()
            user = get_member_object(usernamme)
            FamilyMember.unblock_member(CURRENT_MEMBER, user)
            main_menu()

        elif select_mode == 8:
            print("Logging out...")
            time.sleep(0.6)
            print("---------------------------------------------")
            os.system("python main.py")


        else:
            print("Invalid Choice")
            main_menu()
    else:
        print("1-PURCHASE     2-VIEW BALANCE      3-Request\n")
        print("                 4-LOGOUT\n")
        select_mode = int(input("Enter your Choice: "))
        if select_mode == 1:
            item = input("Enter the Item name: ")
            price = int(input("Enter the price: ").split("$")[0])
            store_name = input("Enter the Store name: ")
            transactions.append(Transaction(CURRENT_MEMBER, price, store_name, item))
            main_menu()

        elif select_mode == 2:
            print("Your Current Balance is", str(CURRENT_MEMBER.wallet.balance) + "$")
            main_menu()

        elif select_mode == 3:
            print("Request has been sent to Dad and Mom")
            add_request(CURRENT_MEMBER)
            main_menu()

        elif select_mode == 4:
            print("Logging out...")
            time.sleep(0.6)
            print("---------------------------------------------")
            os.system("python main.py")

        else:
            print("Invalid Choice")
            main_menu()


if __name__ == "__main__":
    main_menu()
