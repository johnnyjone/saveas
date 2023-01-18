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
indecolo = [A,B,C,D,E,F,G]

a = [["Orange", "ORA.PA"], ["Kering", "KER.PA"], ["L'Oréal", "OR.PA"]]
b = [["Schneider Electric", "SU.PA"], ["Michelin", "ML.PA"], ["EssilorLuxottica", "EL.PA"], ["Dassault Systèmes", "DSY.PA"], 
     ["Capgemini", "CAP.PA"], ["Axa", "CS.PA"], ["Alstom", "ALO.PA"]]  
c = [["Safran", "SAF.PA"], ["LVMH", "MC.PA"], ["Legrand", "LR.PA"], ["Air liquide", "AI.PA"], 
     ["Unibail-Rodamco-Westfield", "URW.AS"], ["Hermès International", "RMS.PA"]]
d = [["Thales", "HO.PA"], ["Stellantis", "STLA.PA"], ["Peugeot", "PEUG.PA"], ["Danone", "BN.PA"], ["TotalEnergies", "TTE.PA"]]
e = [["Crédit agricole", "ACA.PA"], ["Veolia", "VIE.PA"], ["STMicroelectronics", "STM.PA"], ["Renault", "RNO.PA"], ["Engie", "ENGI.PA"], ["Worldline", "WLN.PA"]] 
f = [["Atos", "ATO.PA"], ["Airbus", "AIR.PA"], ["Sanofi", "SAN.PA"], ["BNP Paribas", "BNP.PA"]] 
g = [["Vivendi", "VIV.PA"], ["Teleperformance", "TEP.PA"], ["Publicis Groupe", "PUB.PA"], ["Carrefour", "CA.PA"], ["Société générale", "GLE.PA"]]
h = [["Pernod Ricard", "RI.PA"], ["ArcelorMittal", "MT.AS"], ["Vinci", "DG.PA"], ["Bouygues", "EN.PA"], ["Saint-Gobain", "SGO.PA"]]
indegal = [a,b,c,d,e,f,g,h]
