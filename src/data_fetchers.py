import requests
import pandas as pd
from datetime import datetime, timezone
import logging
import os
from src.utils import format_fecha_actualizacion

logging.basicConfig(level=logging.INFO)

def get_dolar_data():
    url = "https://dolarapi.com/v1/dolares"
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        data = response.json()
        filtered_data = [
            {
                "nombre": item["nombre"],
                "compra": item["compra"],
                "venta": item["venta"],
                "fechaActualizacion": format_fecha_actualizacion(item["fechaActualizacion"])
            }
            for item in data if all(k in item for k in ("nombre", "compra", "venta", "fechaActualizacion"))
        ]
        
        df = pd.DataFrame(filtered_data)
        df.set_index('nombre', inplace=True)
        
        return df
    
    except requests.HTTPError as e:
        logging.error(f"HTTP error: {e}")
    except requests.ConnectionError as e:
        logging.error(f"Connection error: {e}")
    except requests.Timeout as e:
        logging.error(f"Timeout error: {e}")
    except requests.RequestException as e:
        logging.error(f"Request error: {e}")

    return None

def get_crypto_data():
    url = "https://min-api.cryptocompare.com/data/top/mktcapfull"
    params = {
        'limit': 10,
        'tsym': 'USD',
        'api_key': os.getenv('CRYPTOCOMPARE_API_KEY')
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        data = response.json().get('Data', [])
        filtered_data = [
            {
                "Fullname": item["CoinInfo"]["FullName"],
                "Name": item["CoinInfo"]["Name"],
                "PRICE": item["RAW"]["USD"]["PRICE"],
                "TOSYMBOL": item["RAW"]["USD"]["TOSYMBOL"],
                "LASTUPDATE": datetime.fromtimestamp(item["RAW"]["USD"]["LASTUPDATE"], tz=timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
            }
            for item in data 
            if "CoinInfo" in item and "RAW" in item and "USD" in item["RAW"]
        ]
        
        df = pd.DataFrame(filtered_data)
        df.set_index('Name', inplace=True)
        
        return df
    
    except requests.HTTPError as e:
        logging.error(f"HTTP error: {e}")
    except requests.ConnectionError as e:
        logging.error(f"Connection error: {e}")
    except requests.Timeout as e:
        logging.error(f"Timeout error: {e}")
    except requests.RequestException as e:
        logging.error(f"Request error: {e}")

    return None
