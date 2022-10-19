![A picture containing logo Description automatically
generated](media/image1.png)
**Gina Cody School of Engineering and Computer Science**

**Department of Electrical and Computer Engineering**

**COEN 6311 - Software Engineering**

**Mini Programming Project**

**Report By**

**Mohamed Nabeel Deen-40226125**

**TABLE OF CONTENTS**

1.  **PROJECT DESCRIPTION 3**

2.  **USER STORY 3**

3.  **DIAGRAM**

    1.  **Timeline 4**

    2.  **Flow Diagram 5**

    3.  **Use Case Diagram 6**

    4.  **Sequence Diagram 7**

    5.  **UML Class Diagram 8**

4.  **OUTPUT OF THE CODE 9-16**


1.  **Project Description**

Building a console wallet for Brad's family where he and his wife Ana
can manage all the purchases done by them and their 8 children. The
wallet is linked to Brad and Ana's bank from which money can be
deposited to the wallet. Brad and Ana can view all the transactions of
the family members listing items, store names, and prices with the
timestamp. Each child will be having a purchase limit of 50\$ per day,
they need to ask permission for every second purchase they do regardless
of the amount of the first purchase. Brad has the privilege to block any
member of the family from using the wallet. Children can request Ana to
approve overpaying more than 50\$, she can accept or reject or transfer
the request to Brad. If the wallet balance is insufficient Brad and Ana
will receive a notification stating, "Wallet balance is below 100\$" and
kids can request a money deposit too.

GitHub URL:
[**https://github.com/MohamedNabeelDeen/Mini_project**](https://github.com/MohamedNabeelDeen/Mini_project)

**Family Usernames:** Dad and Mom: Brad and Ana. Children: Catherine,
David, Eon, Faz, Georgia, Helena, Irene, Jackson.

2.  **User Story**

-   As a father of 8 children, my wife and I need a family wallet linked
    to our bank account from which my wife, myself and my kids can make
    any purchase.

-   As a father, I can view all the transactions with Items purchased,
    and store and price details with the timestamp.

-   As a child, I have a purchase limit of 50\$ per day.

-   As a kid, I request a money deposit if the wallet balance is
    insufficient.

-   As a father, I can block any of my children from using the wallet
    for purchases and unblock them too.

-   As a kid, if I get blocked by my dad from using the wallet I can
    request him to unblock me.

-   As a father, I should receive a notification if the wallet balance
    is below 100\$

-   As a mom, I should receive a notification if the wallet balance is
    below 100\$

-   As a kid, I can only request an overpay from mom if the purchase
    value is more than 50\$.

-   As a mom, I can accept the child\'s overpay request, reject it, or
    transfer it to the dad.

3.  **Diagram**

    1.  **Timeline:**

![A picture containing timeline Description automatically
generated](media/image2.png)

**3.2 Flow Diagram:**

![Diagram Description automatically
generated](media/image3.png)

**3.3 Use case diagram:**

![Diagram Description automatically
generated](media/image4.png)

**3.4 Sequence Diagram:**

![Diagram Description automatically
generated](media/image5.png)

**3.5 UML Class Diagram:**

![Diagram Description automatically
generated](media/image6.png)

4.  **OUTPUT OF THE CODE**

**PARENT**

Login Page

![Shape Description automatically generated with medium
confidence](media/image7.png)

When the user is Father the Home page is shown.

He can choose one of the 8 options

**CASE 1:** if Brad wants to deposit the amount to himself

![Graphical user interface Description automatically generated with
medium confidence](media/image8.png)

Brad wants to deposit the amount to one of the child-Catherine

![Graphical user interface, text, email Description automatically
generated](media/image9.png)

**CASE 2:** if Brad chooses the purchase option

He must enter the Name of the item, the price and the name of the store.

All the details are stored

![Graphical user interface Description automatically generated with
medium confidence](media/image10.png)

If the wallet balance is insufficient output will be "Not enough
Balance"

![Graphical user interface Description automatically
generated](media/image11.png)

**CASE 3:** View all transaction

![Graphical user interface Description automatically
generated](media/image12.png)

**CASE 4:** Current wallet balance

![Text Description automatically generated with medium
confidence](media/image13.png)

**CASE 5:** The notification option has all the
insufficient wallet balances, overpay requests and Block request

![Graphical user interface, text, application, email Description
automatically generated](media/image14.png)

**CASE 6 and CASE 7:** To block and unblock a user which
only the father can do

He must enter the username

![Graphical user interface, text, application, email Description
automatically generated](media/image15.png)

**CASE 8:** Logout, back to the login page

![Graphical user interface, text, application, email Description
automatically generated](media/image16.png)

**[KID**

Login Page

![](media/image17.png)

If the user is a child, the below options are shown.

**CASE 1:** The Child must enter the Name of the item, the
price and the name of the store.

All the details are stored

![Text Description automatically generated with medium
confidence](media/image18.png)

If the user is blocked by the father (Brad)

Then the user won't be able to purchase-Output "You have been blocked by
Dad"

![Graphical user interface Description automatically generated with low
confidence](media/image19.png)
**CASE 2:** Current wallet balance

![Text Description automatically generated with medium
confidence](media/image20.png)

**CASE 3:** Requesting for an overpay![Graphical user
interface, text Description automatically
generated](media/image21.png)
**CASE 4:** Logout, back to the login page

![Graphical user interface, text Description automatically
generated](media/image22.png)
