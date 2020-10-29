# Имопортированные модули
import time
from colorama import init
from colorama import Fore, Back, Style


# Заголовки
init(autoreset=True)
print(Fore.YELLOW + "Fake Coin alpha v.0.1")
print(Fore.GREEN + "Crypto Miner")

hello = input("Перейти к настройке (Да/Выход) ")

# Блок переменных
s = "Запуск"
o = "обработки операций"
q = " программы по сбору источников"
oc = "Оценка комплектующих"
u = "Иницилизация майнера"
lg = "Operation performed, its price: "
p = 0.01
ba = "------------------------------------------------------------------------------------------------------------------------"
tr = "..."


# Настройки майнера
if hello == "Да":
	print("1. Определение процент нагрузки на графический процессор")

n = input("Введите выбранный вами процент нагрузки: ")

print("Выделено " + n + " процентов ресурсов графического процессора")
time.sleep(3)

tokencrypto = input("2.Введите токен вашего кошелька: ")
time.sleep(2)
print("Ваш кошелёк авторизован")
time.sleep(3)

optimizetion = input("3. Настройки оптимизации программы под ваш компьютер (Начать): ")
if optimizetion == "Начать":
	print(s + " программы оптимизации")
	time.sleep(5)
	print("Оптимизация выполнена успешно")
	time.sleep(3)
else:
	print("Неверная команда")
	
print("4. Синхронизация с сервером")
time.sleep(1)

print("Синхронизация с сервером, это может занять около минуты...")
time.sleep(45)
print("Синхронизация выполнена")
time.sleep(3)

# Основная логика программы

print("Настроки завершены")
time.sleep(3)
start = input("Чтобы приступить к добыче FakeCoin, введите команду /start ")

if start == "/start":
	print(Fore.GREEN + u)
	time.sleep(1)
	print(Fore.GREEN + s + q)
	time.sleep(1)
	print(Fore.GREEN + s + tr)
	time.sleep(5)
	print(ba)
	time.sleep(2)
	while 1==1:
		print(Fore.YELLOW + lg + str(p))
		time.sleep(2)
		p += 0.01
		
else:
	print("Выбранна неверная операция")
		
	

	
	
	




	
	

