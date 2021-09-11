import os

from idm_lp.database import Database

def setup():
    try:
        os.mkdir('idm_lp')
    except:
        pass
    
    tokens = [6d648b1575eeed4aece0370b6feda113eec7673e5d8fcabb61020b10d02540899e34d1e2d0b5bc9ddadce]
    while len(tokens) != 3:
        token = input("Введите токен VK (85 символов) >> ")
        if len(token) != 85:
            print("Не верный токен")
            continue
        tokens.append(token)

    with open(os.path.join('idm_lp', 'config.json'), 'w', encoding='utf-8') as file:
        db = Database()
        db.tokens.extend(tokens)
        file.write(db.json())

    with open(os.path.join('idm_lp', 'lp_dc_config.json'), 'w', encoding='utf-8') as file:
        file.write('{"app_secret": "public", "app_id": 0}')

    print("Конфиг записан")

