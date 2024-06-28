from datetime import datetime
import logging

def format_fecha_actualizacion(fecha_str):
    try:
        fecha_dt = datetime.fromisoformat(fecha_str.replace('Z', '+00:00'))
        return fecha_dt.strftime('%Y-%m-%d %H:%M:%S')
    except ValueError as e:
        logging.error(f"Error formateando la fecha: {e}")
        return None

def prepare_email_message(dolar_df, crypto_df):
    dolar_fecha_actualizacion = dolar_df['fechaActualizacion'].iloc[0] if 'fechaActualizacion' in dolar_df.columns else None
    crypto_last_update = crypto_df['LASTUPDATE'].iloc[0] if 'LASTUPDATE' in crypto_df.columns else None

    if 'fechaActualizacion' in dolar_df.columns:
        dolar_df = dolar_df.drop(columns=['fechaActualizacion'])
    if 'LASTUPDATE' in crypto_df.columns:
        crypto_df = crypto_df.drop(columns=['LASTUPDATE'])

    dolar_text = f"Datos del dólar (actualizados al {dolar_fecha_actualizacion}):\n\n"
    dolar_text += "| {:<27} | {:>10} | {:>10} |\n".format("Nombre", "Compra", "Venta")
    dolar_text += "+-----------------------------+------------+------------+\n"
    for index, row in dolar_df.iterrows():
        dolar_text += "| {:<27} | {:>10.2f} | {:>10.2f} |\n".format(index, row['compra'], row['venta'])
    
    dolar_text += "\n"

    crypto_text = f"Datos de criptomonedas (actualizados al {crypto_last_update}):\n\n"
    crypto_text += "| {:<20} | {:<20} | {:>15} | {:<5} |\n".format("Nombre", "Nombre completo", "Precio", "Símbolo")
    crypto_text += "+----------------------+----------------------+-----------------+-------+\n"
    for index, row in crypto_df.iterrows():
        crypto_text += "| {:<20} | {:<20} | {:>15.2f} | {:<5} |\n".format(index, row['Fullname'], row['PRICE'], row['TOSYMBOL'])

    message = f"La cotización del dólar y las principales criptomonedas son:\n\n"
    message += f"{dolar_text}\n{crypto_text}"

    return message
