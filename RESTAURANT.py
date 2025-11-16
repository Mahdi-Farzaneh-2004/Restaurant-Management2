import smtplib
from email.mime.text import MIMEText
from datetime import datetime
#------Decorator------
def login_user(func):
    def wrapper(self, *args, **kwargs):
        if not self.is_login_in:
            print("user not found")
            return
        return func(self, *args, **kwargs)
    return wrapper
#-------(Manager)-------
class Manager:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.is_login_in = False

    def Register(self):
        if self.email == "mahdi@gmail.com" and self.password == 1383:
            self.is_login_in = True
            print("✅ Login successful")

    @login_user
    def dashboard_manager(self):

        def Add_menu():
            def Food_Add():
                try:
                    input_food = str(input("Enter your Food: "))
                    input_price_food = str(input("Enter your Price: "))
                    with open("food.txt", "a", encoding="UTF-8") as f:
                        f.write(f"{input_food.strip()},{input_price_food.strip()}\n")
                        print("✅ Add successful Food")
                except ValueError:
                    print("❌Invalid Choice\n")

            def Fast_Food_Add():
                try:
                    input_fast_food = str(input("Enter your Fast Food: "))
                    input_price_fast_food = str(input("Enter your Price: "))
                    with open("fastfood.txt", "a", encoding="UTF-8") as f:
                        f.write(f"{input_fast_food.strip()},{input_price_fast_food.strip()}\n")
                        print("✅ Add successful FastFood")
                except ValueError:
                    print("❌Invalid Choice\n")

            def Drink_Add():
                try:
                    input_Drink = str(input("Enter your Drink: "))
                    input_price_Drink = str(input("Enter your Price: "))
                    with open("drink.txt", "a", encoding="UTF-8") as f:
                        f.write(f"{input_Drink.strip()},{input_price_Drink.strip()}\n")
                        print("✅ Add successful Drink")
                except ValueError:
                    print("❌ Invalid Choice\n")

            print("\n1.Food\n2.Fast Food\n3.Drink\n4.Exit\n.........")
            input_add = int(input("Enter your choice: "))
            if input_add == 1:
                Food_Add()
            elif input_add == 2:
                Fast_Food_Add()
            elif input_add == 3:
                Drink_Add()
            elif input_add == 4:
                return

        def Remove_menu():
            def Food_Delete():
                try:
                    input_food_to_delete = input("Enter the name of the food to delete: ")
                    with open("food.txt", "r", encoding="utf-8") as f:
                        lines = f.readlines()
                    for i, line in enumerate(lines):
                        food, price = line.strip().split(",")
                        if input_food_to_delete.lower() == food.lower():
                            del lines[i]
                            with open("food.txt", "w", encoding="utf-8") as f:
                                f.writelines(lines)
                            print("✅ Food remove successfully.")
                            break
                    else:
                        print("❌ Food not found.")
                except ValueError:
                    print("❌ Invalid Choice\n")

            def Fast_Food_Delete():
                try:
                    input_fast_food_to_delete = input("Enter the name of the fast food to delete: ")
                    with open("fastfood.txt", "r", encoding="utf-8") as f:
                        lines = f.readlines()
                    for i, line in enumerate(lines):
                        fast_food, price = line.strip().split(",")
                        if input_fast_food_to_delete.lower() == fast_food.lower():
                            del lines[i]
                            with open("fastfood.txt", "w", encoding="utf-8") as f:
                                f.writelines(lines)
                            print("✅ Food remove successfully.")
                            break
                    else:
                        print("❌ Food not found.")
                except ValueError:
                    print("❌ Invalid Choice\n")

            def Drink_Delete():
                try:
                    input_drink_to_delete = input("Enter the name of the drink to delete: ")
                    with open("drink.txt", "r", encoding="utf-8") as f:
                        lines = f.readlines()
                    for i, line in enumerate(lines):
                        drink, price = line.strip().split(",")
                        if input_drink_to_delete.lower() == drink.lower():
                            del lines[i]
                            with open("drink.txt", "w", encoding="utf-8") as f:
                                f.writelines(lines)
                            print("✅ Drink remove successfully.")
                            break
                    else:
                        print("❌ Drink not found.")
                except ValueError:
                    print("❌ Invalid Choice\n")

            print("\n1.Food\n2.Fast Food\n3.Drink\n4.Exit\n.........")
            input_delete = int(input("Enter your choice: "))
            if input_delete == 1:
                Food_Delete()
            elif input_delete == 2:
                Fast_Food_Delete()
            elif input_delete == 3:
                Drink_Delete()
            elif input_delete == 4:
                return

        def User_list():
            with open("user.txt", "r") as f:
                read = f.readlines()
                for x, user in enumerate(read, start=1):
                    print(f"{x}.{user.strip()}")


            

            def Delet_user():
                input_email=str(input("Enter email user: :"))
                with open("user.txt", "r") as f:
                    read = f.readlines()
                for x, user in enumerate(read, start=1):
                    email1, password1 = user.strip().split(",")
                    if input_email.lower() == email1.lower():
                        del read[x - 1]
                    with open("user.txt", "w", encoding="utf-8") as f:
                        f.writelines(read)
                    print("✅ user remove successfully.")
                    break
                else:
                    print("❌ user not found.")                   
            def Add_user():
                try:
                    input_email=str(input("Enter email user: "))
                    input_password=str(input("Enter password user: "))
                    if not email.endswith("@gmail.com"):
                        raise
                    return

                    with open("user.txt","a") as f:
                        f.write(f"{input_email}, {input_password}\n")
                        print("✅ user successful add")
                except:
                    print("❌ Please enter correct info")

            while True:
                print("\n1.Delet user \n2.Add user \n3.Exit")
                input_user=int(input("Enter your choice: "))
                if input_user == 1:
                    Delet_user()
                elif input_user == 2:
                    Add_user()
                elif input_user == 3:
                    return

        def Change_price():
            def Food_Update():
                try:
                    input_food_update = str(input("Enter your Food: "))
                    input_price_food_update = str(input("Enter your  new Price: "))
                    with open("food.txt", "r", encoding="UTF-8") as f:
                        lines = f.readlines()
                    newline = [f"{food},{input_price_food_update}\n" if input_food_update.lower() == food.lower() else line for line in lines for food, price in [line.strip().split(",")]]
                    if lines == newline:
                        print("❌ food not found\n")
                    else:
                        with open("food.txt", "w", encoding="UTF-8") as f:
                            f.writelines(newline)
                        print("✅ food updated\n")
                except ValueError:
                    print("❌ Invalid Choice\n")

            def Fast_Food_Update():
                try:
                    input_fast_food_update = str(input("Enter your Food: "))
                    input_price_fast_food_update = str(input("Enter your  new Price: "))
                    with open("fastfood.txt", "r", encoding="UTF-8") as f:
                        lines = f.readlines()
                    newline = [f"{food},{input_price_fast_food_update}\n" if input_fast_food_update.lower() == food.lower() else line for line in lines for food, price in [line.strip().split(",")]]
                    if lines == newline:
                        print("❌ fastfood not found\n")
                    else:
                        with open("fastfood.txt", "w", encoding="UTF-8") as f:
                            f.writelines(newline)
                        print("✅ fastfood updated\n")
                except ValueError:
                    print("❌ Invalid Choice\n")

            def Drink_Update():
                try:
                    input_drink_update = str(input("Enter your Food: "))
                    input_price_drink_update = str(input("Enter your  new Price: "))
                    with open("drink.txt", "r", encoding="UTF-8") as f:
                        lines = f.readlines()
                    newline = [f"{food},{input_price_drink_update}\n" if input_drink_update.lower() == food.lower() else line for line in lines for food, price in [line.strip().split(",")]]
                    if lines == newline:
                        print("❌ drink not found\n")
                    else:
                        with open("drink.txt", "w", encoding="UTF-8") as f:
                            f.writelines(newline)
                        print("✅ drink updated\n")
                except ValueError:
                    print("❌ Invalid Choice\n")

            print("\n1.Food\n2.Fast Food\n3.Drink\n4.Exit\n.........")
            input_update = int(input("Enter your choice: "))
            if input_update == 1:
                Food_Update()
            elif input_update == 2:
                Fast_Food_Update()
            elif input_update == 3:
                Drink_Update()
            elif input_update == 4:
                return

        while True:
            print("\nManager Panel \n1.Add Menu \n2.Remove Menu \n3.User list \n4.Change Price \n5.Exit")
            input_manager = int(input("Enter your number : "))
            if input_manager == 1:
                Add_menu()
            elif input_manager == 2:
                Remove_menu()
            elif input_manager == 3:
                User_list()
            elif input_manager == 4:
                Change_price()
            elif input_manager == 5:
                break
#-------User-------
class User():

    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.is_login_in = False

    def Register(self):
        with open("user.txt", "r") as f:
            read = f.readlines()
            found = False
            for user in read:
                emailuser, passworduser = [p.strip() for p in user.split(",")]
                if self.email == emailuser and str(self.password) == passworduser:
                    self.is_login_in = True
                    print("✅ User Found")
                    found = True
                    break

            if not found:
                with open("user.txt", "a") as f:
                    f.write(f"{self.email},{self.password}\n")
                    print("✅ user successful add \nlogin again")

    @login_user
    def dashboard_user(self):
        def Food():
            with open("food.txt", "r") as f:
                lines = f.readlines()
                if not lines:
                    print("Menu is empty")
                    return
                for index, line in enumerate(lines, start=1):
                    food, price = line.strip().split(",")
                    print(f"{index}.{food}----->{price}")
            while True:
                print("\n1.Order \n2.Exit")
                input_Food=int(input("Enter your choice: "))
                if input_Food == 1:
                    order()
                elif input_Food == 2:
                    return

        def FastFood():
            with open("fastfood.txt","r") as f:
                lines1 = f.readlines()
                if not lines1:
                    print("Menu is empty")
                    return
                for index, line in enumerate(lines1, start=1):
                    FastFood, price =line.split(",").strip()
                    print(f"{index}.{FastFood}----->{price}")
            while True:
                print(f"\n1.Order \n2.Exit")
                input_FastFood=int(input("Enter your choice: "))
                if input_FastFood == 1:
                    order()
                elif input_FastFood == 2:
                    return

        def Drink():
            with open("drink.txt", "r") as f:
                lines2 = f.readlines()
                if not lines2:
                    print("Menu is empty")
                    return
                for index, line in enumerate(lines2, start=1):
                    drink, price = line.strip().split(",")
                    print(f"{index}.{drink}----->{price}")
            while True:
                print("\n1.Order \n2.Exit")
                input_Food=int(input("Enter your choice: "))
                if input_Food == 1:
                    order()
                elif input_Food == 2:
                    return

        def order():
            while True:
                input_order=str(input("Enter your number(1, 2,..): "))
                input_ph=int(input("Enter your phonenumber:+98 "))
                input_info=str(input("Enetr your full address(f.e:street, NO.12345) : "))
                send(input_order, input_ph, input_info)
                print("سفارش شما با موفقیت ارسال شد ✅")
                print("\n1.Exit")
                i=int(input("Enter your choice: "))
                if i == 1:
                    exit(1)
                

        def send(input_order, input_ph, input_info):
            sender = "mahdifarzaneh19@gmail.com"
            password = "mitbxxehxgtdoyka"
            receiver = "farzanehmahdi2004@gmail.com"

            html =  f"""<!doctype html>
<html lang="fa">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>New Order</title>
  <style>
    body {{ margin:0; padding:0; background:#f2f4f6; font-family: "Helvetica Neue", Arial, sans-serif; color:#333333; }}
    .wrapper {{ width:100%; table-layout:fixed; background:#f2f4f6; padding:20px 0; }}
    .main {{ background:#ffffff; width:600px; margin:0 auto; border-radius:8px; overflow:hidden; box-shadow:0 2px 6px rgba(0,0,0,0.08); }}
    .header {{ background: linear-gradient(90deg,#ff7a18,#ff3d6b); color:#fff; padding:18px 24px; text-align:right; }}
    .logo {{ font-weight:700; letter-spacing:1px; font-size:20px; }}
    .hero {{ padding:18px 24px; text-align:right; direction:rtl; }}
    .hero h1 {{ margin:0 0 8px; font-size:20px; color:#222; }}
    .hero p {{ margin:0; color:#555; font-size:14px; line-height:1.4; }}
    .card {{ padding:12px 18px; margin:12px 24px; border-radius:6px; background:#fbfbfd; border:1px solid #eef0f5; }}
    .order-meta {{ display:flex; justify-content:space-between; gap:10px; direction:rtl; }}
    .meta-item {{ font-size:13px; color:#666; }}
    .items {{ margin-top:10px; width:100%; border-collapse:collapse; direction:rtl; }}
    .items th, .items td {{ padding:8px 6px; text-align:right; font-size:13px; border-bottom:1px dashed #eceff4; }}
    .items th {{ color:#888; font-weight:600; }}
    .total {{ text-align:right; margin-top:10px; font-weight:700; font-size:15px; color:#222; }}
    .cta {{ display:block; width:220px; margin:18px auto 24px; text-decoration:none; text-align:center; padding:12px 16px; border-radius:6px; background:#ff3d6b; color:#fff; font-weight:700; }}
    .footer {{ font-size:12px; color:#999; text-align:center; padding:14px 20px; }}
    @media only screen and (max-width:620px) {{
      .main {{ width:95% !important; }}
      .order-meta {{ flex-direction:column; align-items:flex-end; }}
    }}
  </style>
</head>
<body>
  <center class="wrapper">
    <table class="main" role="presentation" cellpadding="0" cellspacing="0" width="600">
      <tr>
        <td class="header" align="right" style="direction:rtl">
          <div class="logo">Restaurant • سفارش جدید</div>
        </td>
      </tr>

      <tr>
        <td class="hero">
          <h1>سفارش جدید دریافت شد ✅</h1>
          <p>اطلاعات سفارش در زیر آمده است — برای مشاهده جزئیات یا تأیید سفارش روی دکمهٔ پایین کلیک کنید.</p>
        </td>
      </tr>

      <tr>
        <td>
          <div class="card" style="direction:rtl; text-align:right">
            <!-- Order meta -->
            <div class="order-meta">
              <div class="meta-item"><strong>سفارش:</strong> {input_order}</div>
              <div class="meta-item"><strong>تاریخ:</strong> {datetime.now()}</div>
              <div class="meta-item"><strong>تلفن:</strong> {input_ph}</div>
            </div>

            <!-- Items table -->
            <table class="items" role="presentation" cellpadding="0" cellspacing="0" width="100%">
              <thead>
                <tr>
                  <th style="width:60%;">آیتم</th>
                  <th style="width:20%;">تعداد</th>
                  <th style="width:20%;">قیمت</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>Selected Item</td>
                  <td>1</td>
                  <td>-</td>
                </tr>
              </tbody>
            </table>

            <div class="total">آدرس: {input_info}</div>
            <div class="total">جمع کل: <span style="color:#ff3d6b">-</span></div>
          </div>
        </td>
      </tr>

      <tr>
        <td>
          <a href="#" class="cta">مشاهده سفارش در پنل مدیریت</a>
        </td>
      </tr>

      <tr>
        <td class="footer">
          <div>Restaurant • تماس: +98 912 000 0000</div>
          <div>این ایمیل به‌صورت خودکار تولید شده است — لطفاً پاسخ مستقیم ندهید.</div>
        </td>
      </tr>
    </table>
  </center>
</body>
</html>"""


            msg=MIMEText(html, "html")
            msg["Subject"] = "New order"
            msg["From"] = sender
            msg["To"] = receiver

            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(sender, password)
                server.send_message(msg)

        while True:
            n, a, e=self.email.partition("@")
            print(f"\n{n.title()}'s User Panel \n1.Food \n2.FastFod \n3.Drink \n4.Exit")
            input_manager = int(input("Enter your number : "))
            if input_manager == 1:
                Food()
            elif input_manager == 2:
                FastFood()
            elif input_manager == 3:
                Drink()
            elif input_manager == 4:
                break


#-------This function starts the program-------
def first():
    while True:
        try:
            role = str(input("Are you manager or user(Type manager or user): ")).strip().lower()
            if role not in ("user", "manager"):
                raise
            email = str(input("Enter your email: ")).strip().lower()
            if not email.endswith("@gmail.com"):
                raise
            break
        except:
            print("❌ Please enter correct info")

    password = int(input("Enter your password: "))
    if role == "manager":
        m = Manager(email, password)
        m.Register()
        m.dashboard_manager()
    elif role == "user":
        n = User(email, password)
        n.Register()
        n.dashboard_user()


if __name__ == "__main__":
    first()
