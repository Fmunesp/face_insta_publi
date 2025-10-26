import os
import requests
import json

def publicar_en_facebook(mensaje: str):
    """
    Publica un mensaje en el feed de una página de Facebook usando la Graph API.
    """
    PAGE_ID = "891165894071463"
    ACCESS_TOKEN = os.getenv("FACEBOOK_ACCESS_TOKEN")  # Token en variable de entorno

    if not ACCESS_TOKEN:
        raise ValueError("❌ No se encontró el token de acceso (FACEBOOK_ACCESS_TOKEN).")

    url = f"https://graph.facebook.com/v24.0/{PAGE_ID}/feed"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }
    payload = {"message": mensaje}

    print(f"📤 Enviando mensaje a Facebook: {mensaje}")
    response = requests.post(url, headers=headers, json=payload)

    if response.status_code != 200:
        print("⚠️ Error al publicar:")
        print(response.status_code, response.text)
        return None

    data = response.json()
    print("✅ Publicación realizada correctamente:")
    print(json.dumps(data, indent=2))
    return data


def main():
    mensaje = input("Introduce el post: ")
    publicar_en_facebook(mensaje)


if __name__ == "__main__":
    main()