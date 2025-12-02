import os
import requests
import json

def publicar_en_facebook(link: str):
    """
    Publica un mensaje en el feed de una página de Facebook usando la Graph API.
    """
    PAGE_ID = "891165894071463"
    ACCESS_TOKEN = os.getenv("FACEBOOK_ACCESS_TOKEN")  # Token en variable de entorno

    if not ACCESS_TOKEN:
        raise ValueError("❌ No se encontró el token de acceso (FACEBOOK_ACCESS_TOKEN).")

    url = f"https://graph.facebook.com/v24.0/{PAGE_ID}/photos"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }
    payload = {"url": link}

    print(f"📤 Enviando mensaje a Facebook: {link}")
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
    link = "https://imgs.search.brave.com/-0sRjnVX3QkqebVp7Fc0LNbxYymltTrGz6oPVED347E/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvMTQ2/MzQ1NjgxOS9lcy9m/b3RvL21hbmlwdWxh/dGluZy1iaWctZGF0/YS5qcGc_cz02MTJ4/NjEyJnc9MCZrPTIw/JmM9RXVnSWxPX215/UmNuaTJqeDdsZU10/OGhlZS1QMU5tcWFY/c0pWNXFTN1Bsaz0"
    publicar_en_facebook(link)


if __name__ == "__main__":
    main()