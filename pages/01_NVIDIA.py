import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.markdown('## ¿Porqué NVIDIA?')

st.markdown('''
NVIDIA es una empresa líder en tecnología, con un fuerte enfoque en la innovación y el desarrollo de tecnologías
avanzadas como la inteligencia artificial, la robótica y los vehículos autónomos. Además, NVIDIA ha experimentado un 
crecimiento significativo en los últimos años y ha demostrado una capacidad para superar a sus competidores en términos
de innovación y desempeño financiero. Por lo tanto, invertir en NVIDIA puede ser una buena opción para aquellos que 
buscan invertir en una empresa con potencial de crecimiento a largo plazo en una industria en constante evolución.
''')

df_nvidia = pd.read_csv('./NVIDIA.csv')

st.markdown('Datos obtenidos desde Yahoo Finance')

if st.checkbox('Mostrar DF'):
    st.dataframe(df_nvidia)
    
st.markdown('''
Se puede observar en el gráfico del cierre ajustado de la empresa que su precio ha ido en constante aumento desde el 
2016, presentando un alto potencial de crecimiento.
''')

# Gráfico de la evolución del S&P 500
df_nvidia['Fecha'] = pd.to_datetime(df_nvidia['Fecha'])
df_nvidia = df_nvidia.set_index('Fecha')
st.subheader('Cierre Ajustado histórico del S&P 500')
st.line_chart(df_nvidia['Cierre Ajustado'])

# KPI 1

st.markdown('''<h3>KPI 1: Tasa de crecimiento anual compuesta (CAGR) de los ingresos anuales de Nvidia</h3>''', unsafe_allow_html=True)

st.markdown('''
Se puede observar que cuenta con una Tasa de Crecimiento Anual Compuesta del 11%, lo que significa que ha mantenido un crecimiento estable a lo largo del tiempo.
''')

# Crear un nuevo DataFrame para los ingresos anuales
nvda_ingresos = pd.DataFrame()

# Agregar la columna de ingresos anuales al nuevo DataFrame
nvda_ingresos['Ingresos Anuales'] = df_nvidia['Cierre Ajustado'].resample('Y').mean() * df_nvidia['Volumen'].resample('Y').sum()

# Agregar la columna de años al nuevo DataFrame
nvda_ingresos['Año'] = nvda_ingresos.index.year

# Calcular la tasa de crecimiento anual compuesta (CAGR) de los ingresos anuales de Nvidia
num_anos = len(nvda_ingresos)  # número de años en los que se tienen ingresos anuales
primer_ingreso = nvda_ingresos.iloc[0]['Ingresos Anuales']  # ingresos anuales del primer año
ultimo_ingreso = nvda_ingresos.iloc[-1]['Ingresos Anuales']  # ingresos anuales del último año
cagr = ((ultimo_ingreso / primer_ingreso) ** (1/num_anos)) - 1
st.write(f"Tasa de crecimiento anual compuesta de los ingresos anuales de Nvidia: {cagr:.2%}")

# Crear el gráfico
st.line_chart(nvda_ingresos.set_index('Año')['Ingresos Anuales'])

st.markdown('''<h3>KPI 2: Rendimiento de la inversión (ROI) de Nvidia</h3>''', unsafe_allow_html=True)

# Calcular ROI
st.markdown('''
Un Retorno Diario del 38%, lo que indica que es una empresa rentable y con un buen desempeño financiero.
''')

# Smuestra el grafico
# Por falta de tiempo se coloco la imagen en su lugar
st.image('./src/NVIDIA_KPI2.PNG')

st.markdown('''<h3>KPI 3: Relación precio-beneficio (P/E Ratio)</h3>''', unsafe_allow_html=True)

st.markdown('''
Su P/E Ratio se encuentra en un 88%, lo que sugiere que la empresa tiene un buen desempeño en comparación con sus competidores.
''')
st.image('./src/NVIDIA_KPI3.PNG')


st.markdown('''
En resumen, al considerar el alto rendimiento y equilibrio de riesgo del S&P 500 y la estabilidad financiera y crecimiento constante de NVIDIA, se puede concluir que invertir en esta empresa es una opción recomendable.
''')

st.markdown('''<h3>"Cuando invertir"</h3>''', unsafe_allow_html=True)

st.markdown('''
Este gráfico podría ayudarte a identificar qué días de la semana históricamente han tenido un mejor rendimiento para invertir en Nvidia. En el eje x del gráfico se muestran los días de la semana y en el eje y se muestra el promedio del precio de cierre ajustado para cada día de la semana en el período de tiempo que se haya utilizado para construir el DataFrame.
''')

# Crear una nueva columna con los días de la semana
df_nvidia['Dias_de_semana'] = df_nvidia.index.weekday
# Calcular el promedio de Cierre Ajustado por día de la semana
promedio_dias_semana = df_nvidia.groupby('Dias_de_semana')['Cierre Ajustado'].mean()

# Crear gráfico de barras
fig, ax = plt.subplots()
ax.bar(promedio_dias_semana.index, promedio_dias_semana.values)
ax.set_xticks([0, 1, 2, 3, 4])
ax.set_xticklabels(['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes'])
ax.set_ylim([0, df_nvidia['Cierre Ajustado'].max() * 1.0])

# Agregar etiquetas con el valor promedio
for i, v in enumerate(promedio_dias_semana.values):
    ax.text(i, v + 0.01 * df_nvidia['Cierre Ajustado'].max(), f'{v:.2f}', ha='center')
    
# Agregar títulos y etiquetas de los ejes
ax.set_title('Promedio de Cierre Ajustado por dia de la semana')
ax.set_xlabel('Dias de la semana')
ax.set_ylabel('Cierre Ajustado')

# Mostrar el gráfico en Streamlit
st.pyplot(fig)


st.markdown('''
Si observas que un día en particular ha tenido un promedio de cierre ajustado significativamente más alto que los demás días de la semana, entonces podría ser una buena señal para invertir en Nvidia en ese día de la semana en particular
''')

st.markdown('''<h3>"CONCLUSIÓN"</h3>''', unsafe_allow_html=True)

st.markdown('''
Luego de analizar los datos presentados, se puede concluir que NVIDIA es una compañía con un fuerte crecimiento en los últimos años, tanto en ingresos como en beneficios. Además, tiene una posición dominante en el mercado de GPU y ha logrado expandirse en otros mercados como la inteligencia artificial y el gaming.

En cuanto a la situación actual, NVIDIA ha sido capaz de mantenerse sólida en el mercado a pesar de la pandemia, con un aumento en los ingresos y beneficios en los últimos trimestres. También ha logrado adquirir empresas clave como Arm, lo que podría darle una ventaja competitiva en el futuro.

Teniendo en cuenta estos factores, invertir en NVIDIA podría ser una buena opción para aquellos que buscan un crecimiento a largo plazo en el mercado de la tecnología. 
''')