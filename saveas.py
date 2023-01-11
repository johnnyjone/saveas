import datetime
import pandas as pd
import yfinance as yf
import streamlit as st



stocks = [
    ["Air liquide", "AI.PA"],
    ["Airbus", "AIR.PA"],
    ["Alstom", "ALO.PA"],
    ["ArcelorMittal", "MT.AS"],
    ["Atos", "ATO.PA"],
    ["Axa", "CS.PA"],
    ["BNP Paribas", "BNP.PA"],
    ["Bouygues", "EN.PA"],
    ["Capgemini", "CAP.PA"],
    ["Carrefour", "CA.PA"],
    ["Crédit agricole", "ACA.PA"],
    ["Danone", "BN.PA"],
    ["Dassault Systèmes", "DSY.PA"],
    ["Engie", "ENGI.PA"],
    ["EssilorLuxottica", "EL.PA"],
    ["Hermès International", "RMS.PA"],
    ["Kering", "KER.PA"],
    ["Legrand", "LR.PA"],
    ["L'Oréal", "OR.PA"],
    ["LVMH", "MC.PA"],
    ["Michelin", "ML.PA"],
    ["Orange", "ORA.PA"],
    ["Pernod Ricard", "RI.PA"],
    ["Peugeot", "PEUG.PA"],
    ["Publicis Groupe", "PUB.PA"],
    ["Renault", "RNO.PA"],
    ["Safran", "SAF.PA"],
    ["Saint-Gobain", "SGO.PA"],
    ["Sanofi", "SAN.PA"],
    ["Schneider Electric", "SU.PA"],
    ["Société générale", "GLE.PA"],
    ["Stellantis", "STLA.PA"],
    ["STMicroelectronics", "STM.PA"],
    ["Teleperformance", "TEP.PA"],
    ["Thales", "HO.PA"],
    ["TotalEnergies", "TTE.PA"],
    ["Unibail-Rodamco-Westfield", "URW.AS"],
    ["Veolia", "VIE.PA"],
    ["Vinci", "DG.PA"],
    ["Vivendi", "VIV.PA"],
    ["Worldline", "WLN.PA"]]

# sort by ticker (because yfinance output is sorted by ticker)
stocks.sort(key=lambda x: x[1])

# Cache the web scrapped data so that it is download only once at startup
@st.cache
def load_data():
    start = datetime.date(2017, 1, 1)
    end = datetime.date(2022, 1, 1)

    # Srap stock prices with yfinance
    prices = yf.download([stocks[i][1] for i in range(len(stocks))], start, end)['Adj Close']

    df = pd.DataFrame(prices)

    # Add stocks names as columns names
    df.columns = [stocks[i][0] for i in range(len(stocks))]

    return df


df = load_data()

st.title('APR')

# Add a sidebar to select stocks to display
names = [stocks[i][0] for i in range(len(stocks))]
names.sort()
st.sidebar.subheader('Filter displayed stocks')
stocks_selection = st.sidebar.multiselect('Select stocks to view', options=names)

# Filter stocks according to user input
df = df.loc[:, df.columns.isin(stocks_selection)]

# Display stocks prices chart
st.line_chart(df)
