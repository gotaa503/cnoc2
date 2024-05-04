import requests
import time
import random
from fake_useragent import UserAgent
from datetime import datetime
import platform
import socket
import datetime
from termcolor import colored
import pyfiglet
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

ascii_banner = pyfiglet.figlet_format("SNOS ACCOUNTA \n for you!")
colored_banner = colored(ascii_banner, color='red') 

print(colored_banner)
device_name = socket.gethostname()
ip_address = socket.gethostbyname(device_name)
current_time = datetime.datetime.now()
print(colored(f"Софт от: https://t.me/BelugaFan0", 'yellow'))
print(colored(f"Устройство: {device_name}", 'red'))
print(colored(f"Время запуска софта: {current_time}", 'cyan'))
print(colored(f"IP-адрес (если стоит ваш, проверьте ваш прокси): {ip_address}", 'yellow'))
print(colored(f"Для отправки жалобы на почту, используйте: furfurfur918@gmail.com, пароль: Dapire2023", 'blue'))
print(colored(f"Для отправки жалобы на support@telegram.org", 'blue'))
print(colored(f"При сноса, можно отменить нажав CTRL + C", 'red'))
print(colored(f"Версия софта: pre-alpha v.0.4", 'red'))
print(colored(f"!!РЕКОМЕНДУЕТСЯ МЕНЯТЬ ПРОКСИ ПОСТОЯННО, ЧТОБЫ РЕАЛЬНО СНОСИТЬ АККАУНТ ЖЕРТВЫ!!", 'red'))

def check_data_files():
    try:
        with open('text.txt', 'r') as text_file:
            text = text_file.read().splitlines()
        with open('num.txt', 'r') as num_file:
            numbers = num_file.read().splitlines()
        with open('users.txt', 'r') as user_file:
            users = user_file.read().splitlines()

        if not text or not numbers or not users:
            print("НЕТ ДАННЫХ, проверьте указанные вами данные.")
            return False
        return True

    except FileNotFoundError:
        print("Ошибка: файлы были удалены / владелец репозитория удалил нужные файлы.")
        return False

def send_email(subject, body):
    try:
        smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_server.ehlo()
        smtp_server.starttls()
        smtp_server.login('furfurfur918@gmail.com', 'Dapire2023')
        
        msg = MIMEMultipart()
        msg['From'] = 'furfurfur918@gmail.com'
        msg['To'] = 'support@telegram.org'
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        smtp_server.send_message(msg)
        smtp_server.quit()
        print(colored("Жалоба успешно отправлена на support@telegram.org", 'green'))
    except Exception as e:
        print(colored(f"Ошибка при отправке жалобы на support@telegram.org: {e}", 'red'))

if not check_data_files():
    exit()

url = 'https://telegram.org/support'
ua = UserAgent()

def send_complaint(text, contact, yukino):
    headers = {
        'User-Agent': ua.random
    }
    payload = {
        'text': text,
        'contact': contact
    }

    try:
        response = requests.post(url, data=payload, headers=headers, timeout=5)
        if response.status_code == 200:
            print(f"\33[92mОтправлено жалоба\n Кол-во (лимит 100000)", yukino, "УЖЕ ОТПРАВЛЕНО\33[0m")
        else:
            print(colored(f"Ошибка отправки, возможно проблема в прокси, либо не правильно указан num.txt:", 'red'))
    except requests.exceptions.RequestException as e:
        print(colored(f"Ошибка, проверьте свой интернет либо прокси: {e}", 'red'))

def send_complaints(choice, limit, text, contact, users):
    yukino = 0
    try:
        while yukino < limit:
            yukino += 1
            if choice == '1':
                chosen_text = random.choice(text)
                chosen_contact = random.choice(contact)
                print(f"Отправка жалобы на номер телефона №{yukino}...")
                send_complaint(chosen_text, chosen_contact, yukino)
            elif choice == '2':
                chosen_text = random.choice(text)
                chosen_user = random.choice(users)
                print(f"Отправка жалобы на пользователя №{yukino}...")
                send_complaint(chosen_text, chosen_user, yukino)
            time.sleep(1)
    except KeyboardInterrupt:
        print("Отменен.")
        main_menu()

def change_phone_number():
    new_number = input("Напишите номер телефона (пример: 79373354915): ")
    with open('num.txt', 'w') as num_file:
        num_file.write(new_number)
    print("Номер телефона успешно изменен.")

def change_username():
    new_username = input("Напишите юзернейм (пример: https://t.me/BelugaFan0): ")
    with open('users.txt', 'w') as user_file:
        user_file.write(new_username)
    print("Юзернейм успешно изменен.")

def main_menu():
    while True:
        choice = input("Выберите вариант сноса \n 1 - по номеру телефона, \n2 - по юзер нейму, \n3 - изменить данные \n: ")
        if choice == '3':
            data_choice = input("Выберите данные для изменения \n 1 - Изменить номер телефона, 2 - Изменить юзернейм \n: ")
            if data_choice == '1':
                change_phone_number()
            elif data_choice == '2':
                change_username()
            else:
                print("Неверный выбор.")
        elif choice == '5':
            send_email("Жалоба на аккаунты Telegram", "Текст жалобы: ...")  # Замените "Текст жалобы: ..."
