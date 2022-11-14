"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")

    #
    # Inserte su código aquí
    #
    df.sexo = df.sexo.str.lower()
    df.tipo_de_emprendimiento = df.tipo_de_emprendimiento.str.lower()
    df.idea_negocio = df.idea_negocio.str.lower().str.replace('_',' ').str.replace('-',' ').str.strip()
    df.barrio = df.barrio.str.lower().str.replace('_',' ').str.replace('-',' ').str.strip()
    df.fecha_de_beneficio = pd.to_datetime(
        df.fecha_de_beneficio,

        #
        # Por defecto False. Cuando no se especifica
        # el formato, infiere el formato de la fecha
        #
        infer_datetime_format=True,

        #
        # Controla el comportamiento ante datos
        # invalidos
        #
        #   * 'raise': genera una excepción
        #   * 'coerce': retorna un NaT
        #   * 'ignore': retorna el mismo valor
        #
        errors='coerce',
    )
    df.fecha_de_beneficio = df.fecha_de_beneficio.dt.strftime("%d-%m-%Y")
    df.monto_del_credito = df.monto_del_credito.str.replace('$','').str.replace(',','').str.replace('.00','').str.strip()
    df.línea_credito = df.línea_credito.str.lower().str.replace('-','').str.replace('_',' ').str.replace(' ','').str.strip()
    df.notna()
    df.drop_duplicates(inplace=True)
    print(df.sexo.value_counts().to_list())
    return df

clean_data()