import requests
import json

def get_exchange_rate(currency):
    """Obtiene el tipo de cambio de una moneda dada.

    Args:
        currency (str): El código de la moneda (e.g., 'EUR', 'CNY').

    Returns:
        float: El valor de cambio de la moneda, o None si ocurre un error.
    """

    url = "https://bcv-exchange-rates.vercel.app/get_exchange_rates"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Levanta una excepción si la solicitud falla
        data = json.loads(response.text)
        return data['data'][currency]['value']
    except (requests.exceptions.RequestException, KeyError) as e:
        print(f"Error al obtener el tipo de cambio: {e}")
        return None

if __name__ == "__main__":
    currency = input("Ingrese el código de la moneda (euro, yuan, lira, rublo, dolar): ")
    currency.lower()
    exchange_rate = get_exchange_rate(currency)
    if exchange_rate is not None:
        print(f"El tipo de cambio del {currency} es: {exchange_rate}")
    else:
        print("Moneda no encontrada o error en la solicitud.")
