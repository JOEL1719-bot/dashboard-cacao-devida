
import streamlit as st
import pandas as pd
import plotly.express as px
st.set_page_config(page_title="DEVIDA | Actividad Cacao",page_icon="🌿",layout="wide")
st.markdown("""<style>.block-container{padding-top:1.4rem}h1,h2,h3{color:#145637}[data-testid='stMetric']{background:#eff7f1;border:1px solid #d7e8db;padding:16px;border-radius:12px}</style>""",unsafe_allow_html=True)
st.title("🌿 ACTIVIDAD CACAO | DEVIDA")
st.caption("Oficina Zonal Tingo María · Fuente: dash(5).xlsx · Archivo actualizado hasta octubre de 2026")
st.warning("VERSIÓN DE VALIDACIÓN. La métrica de hectáreas usa la suma de TOTAL (columna V), conforme a la consulta del gráfico principal del PBIX; las demás medidas todavía requieren conciliación con el informe oficial. No confundir asistencias con personas únicas. La hoja principal no contiene fechas mensuales por productor.")
df=pd.read_csv('datos_publicos_personal.csv').fillna(0)
st.sidebar.header('FILTROS')
# Cascada: cada selección reduce las opciones disponibles en los siguientes filtros.
d=df.copy()
for campo,etiqueta,default in [
    ('ambito','Ámbito','Todos'),
    ('comunidad','Comunidad','Todas'),
    ('supervisor','Supervisor','Todos'),
    ('extensionista','Extensionista','Todos'),
    ('tecnico','Técnico','Todos'),
]:
    opciones=sorted(d[campo].dropna().astype(str).unique().tolist())
    seleccion=st.sidebar.selectbox(etiqueta,[default]+opciones,key='filtro_'+campo)
    if seleccion!=default:
        d=d[d[campo]==seleccion]
st.sidebar.markdown('**Corte de los datos:** octubre de 2026')
st.sidebar.caption('Las comunidades con menos de 10 registros por grupo de personal se presentan agrupadas.')
st.sidebar.warning('Los filtros muestran nombre y primer apellido del personal. Verificar autorización institucional antes de difundir el enlace.')
st.sidebar.info('El filtro por mes sigue pendiente: la Hoja 1 no contiene una fecha mensual verificable por productor.')
def total(k):return float(d[k].sum())
def cards(pairs):
 cols=st.columns(len(pairs))
 for c,(title,k,fmt) in zip(cols,pairs):c.metric(title,format(total(k),fmt))
def chart(title,keys,labels=None):
 frame=d.groupby('ambito',as_index=False)[keys].sum()[['ambito']+keys].melt('ambito',var_name='Indicador',value_name='Valor')
 if labels:frame['Indicador']=frame['Indicador'].replace(labels)
 fig=px.bar(frame,x='ambito',y='Valor',color='Indicador',barmode='group',title=title)
 fig.update_layout(xaxis_title='Ámbito',yaxis_title='',legend_title='',height=440)
 st.plotly_chart(fig,use_container_width=True)
def note():st.caption('Cifras exploratorias sumadas por ámbito. Validar unidades, metas y cálculos originales antes de uso oficial.')
tabs=st.tabs(['RESUMEN','CAPACITACIÓN','ATP','ABONOS ORG.','FOLIARES','POSCOSECHA','% FRUTOS'])
with tabs[0]:
 st.subheader('Resumen de la actividad')
 cards([('Registros (no familias únicas)','registros',',.0f'),('Familias (suma del campo)','familias_base_suma',',.0f'),('Hectáreas asistidas (TOTAL - Power BI)','hectareas_asistidas',',.2f'),('Visitas técnicas (suma)','visitas_tecnicas',',.0f')])
 chart('Hectáreas asistidas por ámbito (TOTAL)',['hectareas_asistidas'])
 note()
with tabs[1]:
 st.subheader('Capacitación')
 cards([('Asistencias ECA (suma)','eca_asistencias',',.0f'),('Asistencias CTG (suma)','ctg_asistencias',',.0f')])
 chart('Registros de asistencia por ámbito',['eca_asistencias','ctg_asistencias'],{'eca_asistencias':'ECA','ctg_asistencias':'CTG'})
 st.info('ECA y CTG representan sumas de asistencias; no se presentan como familias únicas.')
with tabs[2]:
 st.subheader('Asistencia técnica personalizada')
 cards([('Visitas técnicas','visitas_tecnicas',',.0f'),('Extensión agraria (suma)','extension_agraria_suma',',.2f')])
 chart('Visitas técnicas por ámbito',['visitas_tecnicas']);note()
with tabs[3]:
 st.subheader('Abonos orgánicos')
 cards([('Biofermentos producidos (L)','biofermentos_producidos_l',',.0f'),('Biofertilizantes aplicados (L)','biofertilizantes_aplicados_l',',.0f'),('Compost producido (kg)','compost_producido_kg',',.0f')])
 chart('Biofermentos y biofertilizantes (L)',['biofermentos_producidos_l','biofertilizantes_aplicados_l']);note()
with tabs[4]:
 st.subheader('Aplicaciones foliares')
 keys=['humato_l','sulfopotasico_l','cobre_quelatado_l','fosfito_potasio_l','foliar_cbz_l','foliar_pk_l','foliar_completo_l']
 st.dataframe(d.groupby('ambito',as_index=False)[keys].sum()[['ambito']+keys],hide_index=True,use_container_width=True)
 chart('Aplicaciones registradas (litros)',['humato_l','sulfopotasico_l','cobre_quelatado_l']);note()
with tabs[5]:
 st.subheader('Poscosecha')
 cards([('Mantenimiento de módulos (suma)','modulos_poscosecha',',.0f'),('Estimado de producción (suma)','estimado_produccion',',.0f'),('Producción reportada (suma)','produccion_reportada',',.0f')])
 chart('Estimado y producción reportada',['estimado_produccion','produccion_reportada']);note()
with tabs[6]:
 st.subheader('Monitoreo de frutos')
 cards([('Frutos registrados','frutos_total',',.0f'),('Frutos sanos','frutos_sanos',',.0f'),('Frutos enfermos','frutos_enfermos',',.0f')])
 if total('frutos_total')>0:
  st.metric('Porcentaje de frutos enfermos (cálculo agregado)',f"{total('frutos_enfermos')/total('frutos_total')*100:.2f}%")
 chart('Conteo de frutos por ámbito',['frutos_sanos','frutos_enfermos']);note()
st.divider()
st.caption('Este paquete no incluye nombres ni DNI de productores; sí incluye nombre y primer apellido del personal para los filtros. Requiere autorización institucional antes de su difusión.')
