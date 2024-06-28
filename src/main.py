import pandas as pd
from src.data_fetchers import get_dolar_data, get_crypto_data
from src.utils import prepare_email_message
from src.sns_client import send_sns_message
import logging

logging.basicConfig(level=logging.INFO)

def main():
    dolar_df = get_dolar_data()
    crypto_df = get_crypto_data()

    if isinstance(dolar_df, pd.DataFrame) and isinstance(crypto_df, pd.DataFrame):
        email_message = prepare_email_message(dolar_df, crypto_df)
        sns_response = send_sns_message(email_message)
        if sns_response:
            logging.info(f"SNS response: {sns_response}")
    else:
        logging.error("Error: Unable to fetch data.")

if __name__ == "__main__":
    main()
