import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# En cierta ciudad de la provincia de Córdoba se registra el número de nacimientos semanales 
# durante las 52 semanas del año, siendo los siguientes los datos obtenidos:
lista_datos = [6,4,2,8,18,16,10,6,7,5,12,8,9,12,17,11,9,16,2,18,18,16,14,12,7,10,3,11,7,12,5,9,11,15,9,4,2,6,11,7,8,10,15,3,2,13,9,11,17,13,12,8]
df = pd.DataFrame(lista_datos, columns=['Semana'])

# Confeccionar una tabla de distribución de frecuencias como dato simple y otra con intervalos de clase.
# Realizar un gráfico acorde

dato_simple = pd.DataFrame(df.value_counts())
dato_simple = dato_simple.rename(columns={'count': 'fi'})
dato_simple = dato_simple.sort_index() # Ordena por el número de semana
dato_simple['fr'] = df.value_counts(normalize=True)

# Agregamos la columna Frecuencia acumulada creciente 'fac'
dato_simple['fac'] = dato_simple['fi'].cumsum()

# Agregamos la columna Frecuencia acumulada decreciente 'fad' invirtiendo las freciencias -> sumandolas acumulativamente -> invirtiendo el resultado
dato_simple['fad'] = dato_simple['fi'][::-1].cumsum()[::-1]

print('\nTabla de distribución de frecuencias con dato simple')
print(dato_simple)


dato_simple['fi'].plot.bar()
plt.show()
