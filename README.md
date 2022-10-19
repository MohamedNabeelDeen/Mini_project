![A picture containing logo Description automatically
generated](./media/image1.png){width="2.7055555555555557in"
height="0.8930555555555556in"}

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

```{=html}
<!-- -->
```
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
generated](./media/media/image2.png){width="9.901785870516186in"
height="3.115236220472441in"}

**3.2 Flow Diagram:**

![Diagram Description automatically
generated](./media/media/image3.png){width="9.939458661417323in"
height="5.598215223097113in"}

**3.3 Use case diagram:**

![Diagram Description automatically
generated](./media/media/image4.png){width="7.848214129483814in"
height="6.0730238407699035in"}

**3.4 Sequence Diagram:**

![Diagram Description automatically
generated](./media/media/image5.png){width="10.525445100612423in"
height="5.410714129483814in"}

**3.5 UML Class Diagram:**

![Diagram Description automatically
generated](./media/media/image6.png){width="10.0in"
height="6.688888888888889in"}

4.  **OUTPUT OF THE CODE**

**PARENT**

Login Page

![Shape Description automatically generated with medium
confidence](./media/media/image7.png){width="6.5in"
height="0.9131944444444444in"}

When the user is Father the Home page is shown.

He can choose one of the 8 options

**[CASE 1:]{.underline}** if Brad wants to deposit the amount to himself

![Graphical user interface Description automatically generated with
medium confidence](./media/media/image8.png){width="6.5in"
height="1.6708333333333334in"}

Brad wants to deposit the amount to one of the child-Catherine

![Graphical user interface, text, email Description automatically
generated](./media/media/image9.png){width="6.5in"
height="2.463888888888889in"}

**[CASE 2:]{.underline}** if Brad chooses the purchase option

He must enter the Name of the item, the price and the name of the store.

All the details are stored

![Graphical user interface Description automatically generated with
medium confidence](./media/media/image10.png){width="6.5in"
height="1.792361111111111in"}

If the wallet balance is insufficient output will be "Not enough
Balance"

![Graphical user interface Description automatically
generated](./media/media/image11.png){width="6.5in"
height="1.8576388888888888in"}

**[CASE 3]{.underline}:** View all transaction

![Graphical user interface Description automatically
generated](./media/media/image12.png){width="7.76423009623797in"
height="3.219335083114611in"}

**[CASE 4:]{.underline}** Current wallet balance

![Text Description automatically generated with medium
confidence](./media/media/image13.png){width="6.5in"
height="1.3569444444444445in"}

**[CASE 5:]{.underline}** The notification option has all the
insufficient wallet balances, overpay requests and Block request

![Graphical user interface, text, application, email Description
automatically generated](./media/media/image14.png){width="10.0in"
height="4.745138888888889in"}

**[CASE 6 and CASE 7:]{.underline}** To block and unblock a user which
only the father can do

He must enter the username

![Graphical user interface, text, application, email Description
automatically generated](./media/media/image15.png){width="6.5in"
height="2.6694444444444443in"}

**[CASE 8:]{.underline}** Logout, back to the login page

![Graphical user interface, text, application, email Description
automatically generated](./media/media/image16.png){width="6.5in"
height="2.479861111111111in"}

**[KID]{.underline}**

Login Page

![](./media/media/image17.png){width="6.5in"
height="0.6777777777777778in"}

If the user is a child, the below options are shown.

**[CASE 1:]{.underline}** The Child must enter the Name of the item, the
price and the name of the store.

All the details are stored

![Text Description automatically generated with medium
confidence](./media/media/image18.png){width="6.5in"
height="1.6520833333333333in"}

If the user is blocked by the father (Brad)

Then the user won't be able to purchase-Output "You have been blocked by
Dad"

![Graphical user interface Description automatically generated with low
confidence](./media/media/image19.png){width="3.9966961942257218in"
height="2.4689621609798773in"}

**[CASE 2:]{.underline}** Current wallet balance

![Text Description automatically generated with medium
confidence](./media/media/image20.png){width="6.5in"
height="1.2930555555555556in"}

**[CASE 3:]{.underline}** Requesting for an overpay![Graphical user
interface, text Description automatically
generated](./media/media/image21.png){width="10.0in"
height="2.6395833333333334in"}

**[CASE 4:]{.underline}** Logout, back to the login page

![Graphical user interface, text Description automatically
generated](./media/media/image22.png){width="6.5in"
height="2.2645833333333334in"}
