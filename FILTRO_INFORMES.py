# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 20:31:25 2021

@author: Catoño
"""

import pandas as pd
import shutil
import os

archivo_2018 = 'D:\CMIM - Proyecto Mamografías\Grupo Deep Learning\INVESTIGACION MARVIN\BD_MARVIN\FILTRO_INFORMES\Listado_Informes_con_imagenes/listado2018.xlsx'
archivo_2019 = 'D:\CMIM - Proyecto Mamografías\Grupo Deep Learning\INVESTIGACION MARVIN\BD_MARVIN\FILTRO_INFORMES\Listado_Informes_con_imagenes/listado2019.xlsx'
archivo_2020 = 'D:\CMIM - Proyecto Mamografías\Grupo Deep Learning\INVESTIGACION MARVIN\BD_MARVIN\FILTRO_INFORMES\Listado_Informes_con_imagenes/listado2020.xlsx'

listado_2018 = pd.read_excel(archivo_2018, sheet_name='Sheet1')
listado_2019 = pd.read_excel(archivo_2019, sheet_name='Sheet1')
listado_2020 = pd.read_excel(archivo_2020, sheet_name='Sheet1')

source_2018 = r'D:\CMIM - Proyecto Mamografías\Grupo Deep Learning\INVESTIGACION MARVIN\BD_MARVIN\FILTRO_INFORMES\2018\\'
source_2019 = r'D:\CMIM - Proyecto Mamografías\Grupo Deep Learning\INVESTIGACION MARVIN\BD_MARVIN\FILTRO_INFORMES\2019\\'
source_2020 = r'D:\CMIM - Proyecto Mamografías\Grupo Deep Learning\INVESTIGACION MARVIN\BD_MARVIN\FILTRO_INFORMES\2020\\'

destination = r'D:\CMIM - Proyecto Mamografías\Grupo Deep Learning\INVESTIGACION MARVIN\BD_MARVIN\FILTRO_INFORMES\Informes_con_imagenes\\'

for i in range(0,len(listado_2018)):
    source=source_2018+listado_2018.iloc[i,0]
    destination_report=destination+listado_2018.iloc[i,0]
    shutil.move(source,destination)
    
for i in range(0,len(listado_2019)):
    source=source_2019+listado_2019.iloc[i,0]
    destination_report=destination+listado_2019.iloc[i,0]
    shutil.move(source,destination)
    
for i in range(0,len(listado_2020)):
    source=source_2020+listado_2020.iloc[i,0]
    destination_report=destination+listado_2020.iloc[i,0]
    shutil.move(source,destination)
