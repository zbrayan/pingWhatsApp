import ping3
from twilio.rest import Client
import schedule
import time

account_sid = 'ACa136071003369e83b5391a982380282c'
auth_token = '9422c9c95988ce010aa25a16af8db4ce'
client = Client(account_sid, auth_token)

# Número de WhatsApp destino
to_whatsapp_number = 'whatsapp:+14155238886'  # Este es un número de prueba de Twilio

def medir_latencia(host):
    try:
        paquetes_perdidos = 0
        for _ in range(2):  # Intenta 5 veces seguidas
            tiempo_respuesta = ping3.ping(host)
            if tiempo_respuesta is None:
                paquetes_perdidos += 1
            else:
                break

        if paquetes_perdidos >= 2:
                            mensaje = "Error con la Conexión a Internet"
                            enviar_mensaje(mensaje)
        else:
            if tiempo_respuesta is not None:
                print(f"Latencia hacia {host}: {tiempo_respuesta * 1000:.2f} ms")


    except Exception as e:
        print(f"Error al medir la latencia: {e}")

# Función para enviar el mensaje
def enviar_mensaje(mensaje):
    message = client.messages.create(
                              body=mensaje,
                              from_='whatsapp:+14155238886',  # Este es tu número de WhatsApp de Twilio
                              to='whatsapp:+5219141085491'
                          )
    print("Mensaje enviado con éxito a", to_whatsapp_number)


schedule.every(1).seconds.do(lambda: medir_latencia('192.168.0.82'))

while True:
    schedule.run_pending()
    time.sleep(1)
