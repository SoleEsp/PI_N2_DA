import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Analisis del Indice S&P 500')
st.image('https://responsive.fxempire.com/v7/_fxempire_/sites/2/sp500-2.jpg?func=cover&q=70&width=500')


st.sidebar.markdown('Evolucion del Indice S&P 500')
st.markdown('## Introducción')

st.markdown('''
El índice S&P 500 es uno de los índices más importantes y representativos del mercado de valores estadounidense. Este índice está compuesto por 500 de las empresas más grandes del mercado y es utilizado como una medida de la salud del mercado de valores de EE. UU.

En este informe, realizaremos un análisis del índice S&P 500 utilizando datos históricos desde el año 2000 hasta la actualidad
''')

df_sp500 = pd.read_csv('./sp500_ETL.csv')

st.markdown('Datos obtenidos desde Yahoo Finance')

if st.checkbox('Mostrar DF'):
    st.dataframe(df_sp500)

st.markdown('## Evolucion Historica')


st.markdown('''
En general, el índice S&P 500 ha tenido un rendimiento muy sólido desde el año 2000.
Si observamos el gráfico de la evolución del índice, podemos ver que hubo un declive significativo durante la crisis financiera de 2008, pero desde entonces el índice ha ido aumentando gradualmente.
En particular, el período entre 2012 y 2020 fue un período de crecimiento constante para el índice, con algunas correcciones menores en el camino.
''')

# Gráfico de la evolución del S&P 500
df_sp500['Fecha'] = pd.to_datetime(df_sp500['Fecha'])
df_sp500 = df_sp500.set_index('Fecha')
st.subheader('Cierre Ajustado histórico del S&P 500')
st.line_chart(df_sp500['Cierre Ajustado'])

st.markdown('''
El objetivo de este proyecto es analizar la evolución histórica del S&P 500 para determinar si invertir en el
mercado de valores a largo plazo es una estrategia viable. Para esto, se utiliza el precio de cierre ajustado, que es 
el precio de cierre de una acción ajustado por los dividendos y los desdoblamientos de acciones.
''')



st.markdown('''
Además, se realizó un análisis de la distribución de los rendimientos mensuales del S&P 500 utilizando un
`diagrama de caja`. En este diagrama se pudo observar la mediana positiva, lo cual es una buena señal para los inversores
''')

retorno_mensual = df_sp500['Cierre Ajustado'].resample('M').ffill().pct_change()
fig, ax = plt.subplots(figsize=(12,6))
sns.boxplot(x=retorno_mensual.index.year, y=retorno_mensual, color='blue', ax=ax)
ax.set_title('Diagrama de caja de los rendimientos mensuales del S&P 500 desde 2000 hasta 2023')
ax.set_xlabel('Año')
ax.set_ylabel('Rendimiento mensual')
st.pyplot(fig)

st.markdown('''
Sin embargo, también se detectaron algunos `valores atípicos` o `outliers` que podrían indicar meses de alta 
volatilidad en el mercado.
''')

retorno_mensual_verf = df_sp500['Cierre Ajustado'].resample('M').ffill().pct_change()

Q1 = retorno_mensual_verf.quantile(0.25)
Q3 = retorno_mensual_verf.quantile(0.75)
IQR = Q3 - Q1

limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

outliers = retorno_mensual_verf[(retorno_mensual_verf < limite_inferior) | (retorno_mensual_verf > limite_superior)]

st.write('Valores atípicos:')
st.write(outliers)

st.markdown('''
Estos valores se obtienen a partir de un rango intercuartil (IQR) y se consideran atípicos si están por debajo 
del límite inferior (negativo) o por encima del límite superior(positivo), los cuales se calculan a partir de una multiplicación del IQR por
un factor de 1.5.
''')

# Agregamos la información sobre cada fecha
fechas_info = {
    '2002-09-30': 'Durante este mes, el índice S&P 500 tuvo una caída del 10,92%, la mayor caída mensual desde octubre de 1987. Este descenso se debió principalmente a la preocupación por una posible guerra en Irak y la caída de los mercados de todo el mundo causado por el atentado de las torre gemelas.',
    '2008-10-31': 'Este mes es conocido como el "Octubre negro" debido a la gran crisis financiera que se desató en todo el mundo. Durante este mes, el S&P 500 cayó un 16,8% y muchos bancos y empresas de todo el mundo se declararon en bancarrota.',
    '2009-02-28': 'Durante este mes, la economía de Estados Unidos se encontraba en plena recesión debido a la crisis financiera mundial. El índice S&P 500 cayó un 11,01% durante el mes de febrero de 2009.',
    '2011-10-31': 'Durante este mes, el S&P 500 subió un 10,81% debido a la aprobación del segundo rescate financiero de la Unión Europea a Grecia, lo que redujo los temores a una posible crisis de deuda en Europa.',
    '2020-03-31': 'Durante este mes, el S&P 500 sufrió una gran caída debido al impacto de la pandemia de COVID-19 en la economía mundial. El índice cayó un 12,51% durante este mes, lo que representa su peor desempeño mensual desde octubre de 2008.',
    '2020-04-30': 'En este mes, el S&P 500 tuvo una recuperación significativa después de su caída en marzo debido a la pandemia de COVID-19. El índice subió un 12,68% en este mes.',
    '2020-11-30': 'En este mes, el S&P 500 registró un aumento del 10,75% debido a las noticias positivas sobre la eficacia de las vacunas contra el COVID-19 y la victoria de Joe Biden en las elecciones presidenciales de Estados Unidos.'
}

# Creamos una lista de las fechas
fechas = list(fechas_info.keys())

# Creamos un menú desplegable para seleccionar la fecha
fecha_seleccionada = st.selectbox('Para saber que sucedio cada año selecciona una fecha', fechas)

# Agregamos un botón para mostrar u ocultar la información adicional
if st.button('Mostrar información adicional'):
    st.write(fechas_info[fecha_seleccionada])
else:
    st.write('Haz clic en el botón para mostrar la información adicional.')
    
st.markdown('''<h3>Analisis de rendimiento y riesgo</h3>''', unsafe_allow_html=True)

st.markdown('''
El análisis de rendimiento y riesgo es un proceso que permite medir el desempeño de una inversión y evaluar 
el nivel de riesgo asociado. En términos generales, el objetivo de este análisis es determinar si una inversión
es rentable y si el riesgo que implica es adecuado para el inversor.
''')

periodo = st.selectbox("Selecciona el período de tiempo:", ["1 año", "3 años", "5 años", "23 años"])

# Filtrar los datos según el período de tiempo seleccionado
if periodo == "1 año":
    df_filtrado = df_sp500.iloc[-252:]
elif periodo == "3 años":
    df_filtrado = df_sp500.iloc[-3*252:]
elif periodo == "5 años":
    df_filtrado = df_sp500.iloc[-5*252:]
else:
    df_filtrado = df_sp500

# Calcular la tasa de rendimiento diaria
retorno_diario_verificacion = df_filtrado['Cierre Ajustado'].pct_change()

# Calcular la volatilidad anualizada
volatilidad = retorno_diario_verificacion.std() * (252 ** 0.5)

# Calcular el rendimiento anualizado
retorno_anual = (1 + retorno_diario_verificacion.mean()) ** 252 - 1

# Calcular el perfil de riesgo
perfil_de_riesgo = retorno_anual / volatilidad

# Mostrar los resultados
if periodo != "23 años":
    st.write("Resultados para el período de tiempo seleccionado:", periodo)
    st.write("Volatilidad anualizada:", round(volatilidad,2))
    st.write("Rendimiento anualizado:", round(retorno_anual,2))
    st.write("Perfil de riesgo:", round(perfil_de_riesgo,2))
else:
    st.write("Resultados para el período completo de 23 años")
    st.write("Volatilidad anualizada:", round(volatilidad,2))
    st.write("Rendimiento anualizado:", round(retorno_anual,2))
    st.write("Perfil de riesgo:", round(perfil_de_riesgo,2))
    
st.markdown('''
Durante los últimos 23 años, el mercado de valores ha mostrado un rendimiento anualizado positivo (0.07) 
con una volatilidad anualizada relativamente baja (0.2), lo que indica una rentabilidad adecuada para el nivel 
riesgo del inversor (perfil de riesgo de 0.33).

En conjunto, estos resultados muestran que la inversión en el mercado de valores puede ser rentable a largo plazo, 
pero el rendimiento y el nivel de riesgo varían según el período de tiempo seleccionado. 
''')

st.markdown('''<h3>¿Entonces qué nos dice este analisis?</h3>''', unsafe_allow_html=True)

st.markdown('''
El análisis EDA y de rendimiento y riesgo del S&P 500 nos muestra que históricamente ha sido una inversión rentable y relativamente segura en comparación con otros activos financieros. A pesar de las fluctuaciones en el mercado y eventos como la crisis financiera de 2008 y la pandemia de COVID-19, el S&P 500 ha demostrado una tendencia al alza a largo plazo.

Después de analizar el S&P 500 y ver que tiene un alto rendimiento y un equilibrio de riesgo, se decidió invertir en una de las empresas que conforman el índice, `NVIDIA`.
''')