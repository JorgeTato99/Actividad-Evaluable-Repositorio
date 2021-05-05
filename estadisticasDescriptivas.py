# Se importan las librerías necesarias
import pandas as pd

# Se lee el archivo CSV
df = pd.read_csv("ulabox_orders_with_categories_partials_2017.csv")

listaVariablesAEvaluar = ["total_items", "discount%", "weekday", "hour", "Food%", "Fresh%", "Drinks%", "Home%", "Beauty%", "Health%", "Baby%", "Pets%"]

for VariableAEvaluar in listaVariablesAEvaluar:
  print("Datos para:", VariableAEvaluar)
  Media = df[VariableAEvaluar].mean()
  Mediana = df[VariableAEvaluar].median()
  Moda = df[VariableAEvaluar].mode()
  Maximo = df[VariableAEvaluar].max()
  Minimo = df[VariableAEvaluar].min()
  Rango = df[VariableAEvaluar].max() - df[VariableAEvaluar].min()
  Std = df[VariableAEvaluar].std(ddof=0)
  Q1 = df[VariableAEvaluar].quantile(0.25)
  Q2 = df[VariableAEvaluar].quantile(0.50)
  Q3 = df[VariableAEvaluar].quantile(0.75)
  Q4 = df[VariableAEvaluar].quantile(1.00)
  print("== Medidas de Tendencia Central ==")
  print("Media: %.2f" %Media)
  print("Mediana: %.2f" %Mediana)
  print("Moda: %.2f" %Moda)
  print("== Max, Min y Rango ==")
  print("Máximo: %.2f" %Maximo)
  print("Mínimo: %.2f" %Minimo)
  print("Rango: %.2f" %Rango)
  print("== Medidas de Dispersión ==")
  print("Desviación Estándar: %.2f" %Std)
  print("== Medidas de Posición ==")
  print("1° Cuartil: %.2f" %Q1)
  print("2° Cuartil: %.2f" %Q2)
  print("3° Cuartil: %.2f" %Q3)
  print("4° Cuartil: %.2f" %Q4)
  print("\n")