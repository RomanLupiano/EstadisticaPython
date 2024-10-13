import pandas as pd
import matplotlib.pyplot as plt

# Se les pregunta a los empleados de un restaurante de lujo que día de la semana prefieren tomarse libre,
# sabiendo que deben trabajar todos los domingos. Los resultados de las respuestas son los siguientes:
dias = ['L', 'S', 'S', 'S', 'M', 'MI', 'J', 'J', 'L', 'V', 'V', 'V', 'S', 'L', 'S', 'J', 'J', 'S', 'M', 
        'J', 'MI', 'MI', 'L', 'S', 'S', 'MI', 'J', 'MI', 'V', 'S', 'M', 'L', 'M', 'V', 'J', 'V', 'MI', 
        'S', 'M', 'L', 'V', 'V', 'S', 'S', 'S']

# Realizar una tabla de distribución de frecuencias y graficar los datos.

colummas = ['Dias']

tabla = pd.DataFrame(dias, columns=colummas)

# print(tabla) # Imprime todo el dataframe

#print(tabla.info()) # Muestra información del dataframe (Cantidad de datos, cuanto ocupa en total, el tipo de dato, etc)
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 45 entries, 0 to 44
Data columns (total 1 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   Dias    45 non-null     object
dtypes: object(1)
memory usage: 492.0+ bytes
None
'''

#print(tabla.describe()) # Genera estadísticas descriptivas (Cantidad total, valores únicos
'''
       Dias
count    45    # Cantidad total de datos
unique    6    # Cantidad de valores únicos (6 días de la semana)
top       S    # Dato de mayor frecuencia
freq     13    # Frecuencia del top
'''


#print(tabla.value_counts()) # Una tabla de frecuencias
'''
Dias
S       13
V        8
J        7
L        6
MI       6
M        5
Name: count, dtype: int64
'''

#print(tabla.value_counts(normalize=True)) # Una tabla de frecuencias relativas
'''
Dias
S       0.288889
V       0.177778
J       0.155556
L       0.133333
MI      0.133333
M       0.111111
Name: proportion, dtype: float64
'''

# Para construir una tabla de frecuencias e ir agregandole columnas, vamos a guardar en un dataframe el resultado de .value_counts()
tabla_frec = pd.DataFrame(tabla.value_counts())
tabla_frec = tabla_frec.rename(columns={'count': 'fi'})
#print(tabla_frec)
'''
      fi
Dias    
S     13
V      8
J      7
L      6
MI     6
M      5
'''

#Agregamos la columna de frecuencias relativas
tabla_frec["fr"] = tabla.value_counts(normalize=True)
# tabla_frec['fr'] = tabla_frec['fi']/tabla_frec['fi'].sum() # También podría utilizarse esta alternativa
print(tabla_frec)
'''
      fi        fr
Dias              
S     13  0.288889
V      8  0.177778
J      7  0.155556
L      6  0.133333
MI     6  0.133333
M      5  0.111111
'''


#Para graficar se usa matplotlib
tabla_frec['fi'].plot.bar()
plt.show()


tabla_frec['fi'].plot.pie()
plt.show()