import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('./smart_home_energy_usage_dataset.csv')

x=[1,2,3]
y=[5,7,9]

plt.plot(x,y,label="linea1") # creación de la recta
plt.xlabel("Metros cuadrados") #etiqueta eje X
plt.ylabel("Costo en miles de soles") #etiqueta eje Y
plt.title("Relación Costo y m2") #Agregamos un título
plt.legend() #agregamos la leyenda
plt.show() #desplegamos el gráfico


sns.catplot(data=df, x="appliance", y="energy_consumption_kWh",  errorbar=("pi", 95), kind="bar")