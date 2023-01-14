import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

stocks_40 = [
    ["Atos", "ATO.PA"],
    ["Axa", "CS.PA"],  
    ["Capgemini", "CAP.PA"],
    ["Carrefour", "CA.PA"],
    ["EssilorLuxottica", "EL.PA"],
    ["Hermès International", "RMS.PA"],
    ["Kering", "KER.PA"],
    ["L'Oréal", "OR.PA"],
    ["LVMH", "MC.PA"],
    ["Orange", "ORA.PA"],
    ["Publicis Groupe", "PUB.PA"],  
    ["Sanofi", "SAN.PA"],
    ["Stellantis", "STLA.PA"],
    ["Teleperformance", "TEP.PA"],   
    ["Vivendi", "VIV.PA"],
    ["Worldline", "WLN.PA"]]

A = [["Schneider Electric", "SU.PA"], ["Legrand", "LR.PA"]]
B = [["Engie", "ENGI.PA"], ["Unibail-Rodamco-Westfield", "URW.AS"]]
C = [["Veolia", "VIE.PA"], ["Alstom", "ALO.PA"]]
D = [["Michelin", "ML.PA"], ["Bouygues", "EN.PA"], ["Danone", "BN.PA"], ["STMicroelectronics", "STM.PA"], 
     ["Renault", "RNO.PA"], ["Peugeot", "PEUG.PA"], ["Saint-Gobain", "SGO.PA"], ["Pernod Ricard", "RI.PA"], ["Vinci", "DG.PA"]]
E = [["Thales", "HO.PA"], ["Airbus", "AIR.PA"], ["Safran", "SAF.PA"]]
F = [["ArcelorMittal", "MT.AS"], ["Air liquide", "AI.PA"]]
G = [["BNP Paribas", "BNP.PA"], ["Dassault Systèmes", "DSY.PA"], ["Crédit agricole", "ACA.PA"], ["TotalEnergies", "TTE.PA"], ["Société générale", "GLE.PA"]]
