import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
   

A = [["Schneider Electric", "SU.PA"], ["Orange", "ORA.PA"], ["Legrand", "LR.PA"]]
B = [["Engie", "ENGI.PA"], ["EssilorLuxottica", "EL.PA"], ["Unibail-Rodamco-Westfield", "URW.AS"]]
C = [["Veolia", "VIE.PA"], ["Alstom", "ALO.PA"], ["L'Oréal", "OR.PA"], ["Worldline", "WLN.PA"], 
     ["Hermès International", "RMS.PA"], ["Carrefour", "CA.PA"], ["Atos", "ATO.PA"]]
D = [["Michelin", "ML.PA"], ["Bouygues", "EN.PA"], ["Danone", "BN.PA"], ["STMicroelectronics", "STM.PA"], 
     ["Renault", "RNO.PA"], ["Peugeot", "PEUG.PA"], ["Saint-Gobain", "SGO.PA"], ["Pernod Ricard", "RI.PA"], ["Teleperformance", "TEP.PA"],   
     ["Vivendi", "VIV.PA"], ["Publicis Groupe", "PUB.PA"], ["Capgemini", "CAP.PA"], ["Vinci", "DG.PA"]]
E = [["Thales", "HO.PA"], ["Sanofi", "SAN.PA"], ["Axa", "CS.PA"], ["Stellantis", "STLA.PA"], 
     ["Airbus", "AIR.PA"], ["LVMH", "MC.PA"], ["Safran", "SAF.PA"]]
F = [["ArcelorMittal", "MT.AS"], ["Kering", "KER.PA"], ["Air liquide", "AI.PA"]]
G = [["BNP Paribas", "BNP.PA"], ["Dassault Systèmes", "DSY.PA"], ["Crédit agricole", "ACA.PA"], ["TotalEnergies", "TTE.PA"], ["Société générale", "GLE.PA"]]


stocks_40 = [
    ["Air liquide", "AI.PA"],  91
    ["Airbus", "AIR.PA"],  87
    ["Alstom", "ALO.PA"],  94
    ["ArcelorMittal", "MT.AS"],  82
    ["Atos", "ATO.PA"],  86
    ["Axa", "CS.PA"],  93
    ["BNP Paribas", "BNP.PA"],  87
    ["Bouygues", "EN.PA"],  83
    ["Capgemini", "CAP.PA"],  94
    ["Carrefour", "CA.PA"],  85
    ["Crédit agricole", "ACA.PA"],  88
    ["Danone", "BN.PA"],  89
    ["Dassault Systèmes", "DSY.PA"],  94
    ["Engie", "ENGI.PA"],  88
    ["EssilorLuxottica", "EL.PA"],  94
    ["Hermès International", "RMS.PA"],  92
    ["Kering", "KER.PA"],  95
    ["Legrand", "LR.PA"],  91
    ["L'Oréal", "OR.PA"],  95
    ["LVMH", "MC.PA"],  91
    ["Michelin", "ML.PA"], 93
    ["Orange", "ORA.PA"],  99
    ["Pernod Ricard", "RI.PA"], 81
    ["Peugeot", "PEUG.PA"],  89
    ["Publicis Groupe", "PUB.PA"],  84
    ["Renault", "RNO.PA"],  88
    ["Safran", "SAF.PA"],  90
    ["Saint-Gobain", "SGO.PA"],
    ["Sanofi", "SAN.PA"], 87
    ["Schneider Electric", "SU.PA"],  94
    ["Société générale", "GLE.PA"],  86
    ["Stellantis", "STLA.PA"],
    ["STMicroelectronics", "STM.PA"],  88
    ["Teleperformance", "TEP.PA"], 84
    ["Thales", "HO.PA"],  89
    ["TotalEnergies", "TTE.PA"],  90
    ["Unibail-Rodamco-Westfield", "URW.AS"],  92
    ["Veolia", "VIE.PA"],  88
    ["Vinci", "DG.PA"],  83
    ["Vivendi", "VIV.PA"],  84
    ["Worldline", "WLN.PA"]]  88

