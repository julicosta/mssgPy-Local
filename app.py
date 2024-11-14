import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def setup_driver():
    options = Options()
    options.headless = False  # Activa el modo sin encabezado
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Inicializar ChromeDriver en modo sin encabezado
    service = Service("C:\\Users\\julia\\Desktop\\chromedriver-win64\\chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def send_whatsapp_messages(messages):
    # Configuración del driver de Selenium para WhatsApp Web
    driver = setup_driver()

    try:
        # Abre WhatsApp Web
        driver.get("https://web.whatsapp.com")
        print("Esperando para escanear el código QR...")
        time.sleep(50)  # Tiempo para escanear el código QR

        # Enviar los mensajes
        for item in messages:
            phone = item['phone']
            message = item['message']

            try:
                driver.get(f"https://web.whatsapp.com/send?phone={phone}&text={message}")
                time.sleep(10)  # Espera a que se cargue la página

                # Hacer clic en el botón de enviar
                send_button = driver.find_element(By.XPATH, '//span[@data-icon="send"]')
                send_button.click()
                print(f"Mensaje enviado a {phone}")
                time.sleep(5)  # Esperar un momento antes de enviar el siguiente mensaje

            except Exception as e:
                print(f"Error al enviar mensaje a {phone}: {e}")

        print("Mensajes enviados exitosamente")
    
    except Exception as e:
        print(f"Error al iniciar el proceso de envío de mensajes: {e}")
    
    finally:
        driver.quit()

if __name__ == "__main__":
    # Leer mensajes de un archivo JSON local
    with open("messages.json", "r") as file:
        messages = json.load(file)
    
    send_whatsapp_messages(messages)
