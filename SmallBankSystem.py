import pandas as pd
class Bank:
    def __init__(self, balance):
        self.__balance=balance
        self.info=pd.DataFrame({
            "malumot":[
                'ism',
                'familya',
                'yosh',
                'manzil',
                'cardnumber'
            ],
            '.':[
                'Shohrux',
                'Berdiyorov',
                19,
                'Jizzax viloyati, Jizzax shahar',
                '8600 1606 3934 3435'
            ]
        })
    def get_balance(self):
        return self.__balance
    def pul_qushish(self):
        pul = int(input("qancha pul qushmoqchisiz? "))
        if pul > 0:
            self.__balance+=pul
            print(f'yangi balans: {self.__balance}')
        else:
            print("Noto'g'ri summa kiritdingiz")
    def pul_yechish(self):
        pul=int(input("qancha pul yechmoqchisiz? "))
        if pul<=self.__balance:
            self.__balance-=pul
            print(f'yangi balans: {self.__balance}')
        else:
            print("xato summa kiritdingiz")
    def kabinet(self):
        print(self.info)
account1=Bank(5000)
print("Pinkodni kiritng")
while True:
    pinkod=int(input())
    if pinkod==1103:
        break
    else:
        print("Xato pinkod kiritdingiz")
print("xizmatni tanlang")
print("1.Balansni bilish")
print("2.Pul qo'shish")
print("3.Pul yechish")  
print("4.Kabinet")
tanlash=int(input())
if tanlash==1:
    print(f"Sizning hisobingizda {account1.get_balance()} so'm bor")
elif tanlash==2:
    account1.pul_qushish()
elif tanlash==3:
    account1.pul_yechish()
elif tanlash==4:
    account1.kabinet() 
else:
    print("Noto'g'ri xizmat tanladingiz")
