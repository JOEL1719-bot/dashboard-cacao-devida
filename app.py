import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from html import escape
from pathlib import Path
st.set_page_config(page_title='DEVIDA | Actividad Cacao',page_icon='🌿',layout='wide')
st.markdown('''<style>
.block-container{padding-top:.65rem;max-width:1550px;padding-bottom:1.8rem}
.stApp{background:linear-gradient(150deg,#f1f9ff 0%,#ffffff 38%,#f1fff5 100%)}
[data-testid="stSidebar"]{background:linear-gradient(180deg,#e7f5ff,#f2fff6)!important;border-right:2px solid #c2e5ed}
[data-testid="stSidebar"] h2{background:linear-gradient(110deg,#009d4c,#08c76a);color:white!important;padding:14px 18px;border-radius:14px}
[data-testid="stMetric"]{position:relative;overflow:hidden;background:linear-gradient(130deg,#0964a5,#078bc5);border:1px solid #ffffff8c;padding:15px 17px;border-radius:18px;box-shadow:0 5px 13px #0b355026;min-height:102px}
[data-testid="stMetric"]:before{content:'✦';position:absolute;right:10px;top:3px;font-size:48px;color:#ffffff22}
[data-testid="stMetricLabel"]{color:white!important;font-weight:800!important;font-size:14px!important}
[data-testid="stMetricValue"]{color:white!important;font-size:32px!important;font-weight:800!important}
[data-testid="stMetric"] *{color:white!important}
.st-key-resumen_compacto [data-testid="stMetric"]{min-height:96px!important;padding:12px 18px!important}
.st-key-resumen_compacto [data-testid="stMetricValue"]{font-size:30px!important}
.st-key-resumen_compacto [data-testid="stHorizontalBlock"]:nth-of-type(2) [data-testid="stMetric"]{background:linear-gradient(125deg,#078f56,#18c26b)}
.devida-gauge-card{position:relative;height:208px;border:1.5px solid var(--gauge-color);border-radius:20px;background:linear-gradient(160deg,#ffffff 15%,var(--gauge-pale) 100%);padding:11px 12px 7px;box-shadow:0 6px 15px #19395d1b;display:flex;flex-direction:column;align-items:center;justify-content:space-between;margin-bottom:12px;box-sizing:border-box;overflow:hidden}
.devida-gauge-title{font:800 14px/1.2 Arial,sans-serif;text-align:center;color:#ffffff;min-height:32px;width:96%;background:var(--gauge-color);border-radius:18px;padding:8px 5px;display:flex;align-items:center;justify-content:center;box-sizing:border-box;text-shadow:0 1px 1px #00000026}
.devida-gauge-icon{position:absolute;top:76px;left:16%;font-size:36px;line-height:1;z-index:2;filter:drop-shadow(0 3px 2px #0000002c)}
.devida-gauge-card svg{display:block;width:100%;max-width:255px;height:135px;overflow:visible}
.devida-avance{position:absolute;right:12px;bottom:29px;z-index:3;background:#e7f7ed;color:#126b3d;border:1px solid #a7ddbd;border-radius:12px;padding:4px 7px;font:800 13px Arial,sans-serif;white-space:nowrap}
.devida-avance-cap{font-size:20px;padding:7px 11px;bottom:22px;right:14px;border-radius:14px}
.devida-gauge-card:after{content:'';position:absolute;bottom:-24px;left:-30px;width:115px;height:70px;border-radius:50%;background:var(--gauge-color);opacity:.07}
@media(max-width:1050px){.devida-gauge-card{height:194px}.devida-gauge-card svg{height:121px;max-width:235px}.devida-gauge-icon{font-size:31px;top:77px}}
[data-testid="stTabs"] [data-baseweb="tab"]{font-weight:750!important}
[data-testid="stVerticalBlockBorderWrapper"]:has(.devida-gauge-anchor){border-radius:18px!important}
.community-row{display:flex;justify-content:space-between;align-items:center;gap:12px;margin:8px 0 3px;font:600 13px Arial,sans-serif;color:#174365}.community-track{height:9px;background:#e5edf2;border-radius:8px;overflow:hidden}.community-fill{height:100%;border-radius:8px}.compact-kpi{border:1.5px solid var(--accent);background:linear-gradient(145deg,#fff,var(--pale));border-radius:18px;padding:16px 18px;min-height:126px;box-shadow:0 4px 13px #19395d16;margin:5px 0 14px}.compact-kpi-title{font:800 14px Arial,sans-serif;color:#fff;background:var(--accent);border-radius:12px;padding:9px;text-align:center}.compact-kpi-value{font:800 30px Arial,sans-serif;text-align:center;color:#123d61;padding-top:10px}.compact-kpi-note{font:12px Arial,sans-serif;text-align:center;color:#50677c;padding-top:5px}
.cap-target-card{position:relative;min-height:120px;border-radius:19px;background:linear-gradient(130deg,#0964a5,#078bc5);padding:16px 20px;box-shadow:0 5px 13px #0b355026;box-sizing:border-box;overflow:hidden;margin-bottom:12px}
.cap-target-card:before{content:'✦';position:absolute;right:17px;top:15px;font-size:47px;color:#ffffff2b}
.cap-target-title{font:800 15px Arial,sans-serif;color:white;margin-bottom:12px;position:relative}
.cap-target-row{display:flex;align-items:center;justify-content:space-between;gap:12px;position:relative}
.cap-target-value{font:800 34px Arial,sans-serif;color:white}
.cap-target-pct{font:800 20px Arial,sans-serif;background:#e7f7ed;color:#126b3d;border:1px solid #a7ddbd;border-radius:13px;padding:7px 11px;white-space:nowrap}
</style>''',unsafe_allow_html=True)
st.title('🌿 ACTIVIDAD CACAO | DEVIDA')
st.caption('Oficina Zonal Tingo María · OCTUBRE 2026 · JOEL GONZALES R.')
@st.cache_data
def load(file_version):
 return pd.read_csv('indicadores_hoja1_agrupados.csv',encoding='utf-8-sig').fillna(0)
# La fecha de modificación invalida la caché cuando se reemplaza el CSV en GitHub.
d=load(Path('indicadores_hoja1_agrupados.csv').stat().st_mtime_ns)
st.sidebar.header('FILTROS')
# Opciones dependientes: cada selección limita las siguientes listas.
filter_fields=[('ambito','Ámbito','Todos'),('comunidad','Comunidad','Todas'),('supervisor','Supervisor','Todos'),('extensionista','Extensionista','Todos'),('tecnico','Técnico','Todos')]
if 'especialista_poscosecha' in d.columns:
 filter_fields.append(('especialista_poscosecha','Especialista poscosecha','Todos'))

# El buscador se ejecuta antes de crear los selectores, para poder sincronizarlos.
registro=None
with st.sidebar.expander('🔎 BUSCAR PARTICIPANTE', expanded=True):
 st.caption('Cargue su Excel original solo cuando necesite consultar un productor.')
 excel_privado=st.file_uploader('Excel de participantes (Hoja 1)',type=['xlsx'],key='excel_privado')
 if excel_privado is not None:
  try:
   from io import BytesIO
   import unicodedata
   import hashlib
   base_personal=pd.read_excel(BytesIO(excel_privado.getvalue()),sheet_name=0)
   if 'PARTICIPANTE' not in base_personal.columns:
    st.error('No se encontró la columna PARTICIPANTE en Hoja 1.')
   else:
    texto=st.text_input('Escriba nombre o apellido',placeholder='Ejemplo: JUAN PEREZ',key='busqueda_participante')
    if texto.strip():
     def normalizar_nombre(s):
      return ''.join(c for c in unicodedata.normalize('NFKD',str(s).upper()) if not unicodedata.combining(c)).strip()
     terminos=normalizar_nombre(texto).split()
     nombres=base_personal['PARTICIPANTE'].fillna('').astype(str)
     coincidencias=base_personal.loc[nombres.map(lambda n:all(t in normalizar_nombre(n) for t in terminos))].copy()
     if coincidencias.empty:
      st.info('No se encontraron participantes.')
     else:
      opciones=['— Seleccione participante —']
      opciones += [f"{r['PARTICIPANTE']} · {r.get('COMUNIDAD','')} · fila {i+2}" for i,r in coincidencias.iterrows()]
      # Cambiar la búsqueda reinicia la elección anterior.
      widget_key='participante_elegido_'+hashlib.sha256(texto.strip().encode()).hexdigest()[:12]
      # Sin callback: evita referencias obsoletas de Streamlit entre ejecuciones.
      indices=list(coincidencias.index)
      elegido=st.selectbox(f'{len(coincidencias)} coincidencia(s)',opciones,key=widget_key)
      if elegido in opciones[1:]:
       pos=opciones.index(elegido)-1
       if 0 <= pos < len(indices):
        registro=base_personal.loc[indices[pos]]
        for campo,indice_col in [('ambito',2),('comunidad',11),('supervisor',3),('extensionista',6),('tecnico',7),('especialista_poscosecha',4)]:
         if any(campo==f for f,_,_ in filter_fields):
          valor=registro.iloc[indice_col]
          valor_limpio=str(valor).strip() if pd.notna(valor) else ''
          st.session_state['filtro_'+campo]=valor_limpio if valor_limpio else ('Todas' if campo=='comunidad' else 'Todos')
        st.success('Participante seleccionado: '+str(registro['PARTICIPANTE']))
        st.caption('Los filtros se completan automáticamente según el Excel privado.')
  except Exception as exc:
   st.error(f'No se pudo leer el Excel: {exc}')

if st.sidebar.button('↺ Limpiar filtros',width="stretch"):
 for field,_,_ in filter_fields:
  st.session_state.pop('filtro_'+field,None)
 st.session_state.pop('busqueda_participante',None)
 st.rerun()

for field,label,default in filter_fields:
 available=sorted({str(v).strip() for v in d[field].dropna() if str(v).strip() not in ('','0','nan','None')})
 options=[default]+available
 widget_key='filtro_'+field
 # Conservar el valor del Excel privado aunque no figure en el CSV agregado.
 if registro is not None and st.session_state.get(widget_key) not in (None,default) and st.session_state[widget_key] not in options:
  options.append(st.session_state[widget_key])
 if st.session_state.get(widget_key,default) not in options:
  st.session_state[widget_key]=default
 chosen=st.sidebar.selectbox(label,options,key=widget_key)
 if chosen!=default:
  d=d[d[field].astype(str).str.strip()==chosen]

# Si hay un participante elegido, se muestran sus indicadores individuales.
if registro is not None:
  # Convertir la fila individual a las mismas columnas que el CSV agrupado.
  # El resto del dashboard utiliza exactamente sus funciones existentes.
  columnas={
   'atp':33,'poda_mantenimiento':41,'mip_prod':39,'aplic_biofert':43,
   'abonamiento':35,'crecimiento':19,'produccion_ha':20,
   'poda_formacion':36,'mip_crec':37,'abon_fructificacion':40,
   'abon_boton':42,'abon_floracion':44,'mant_biofermentos':46,
   'compost_producido_kg':49,'biofermentos_producidos_l':47,
   'biofertilizantes_aplicados_l':48,'acodos':67,'humato_l':72,
   'sulfopotasico_l':73,'cobre_quelatado_l':74,'fosfito_potasio_l':75,
   'foliar_cbz_l':76,'foliar_pk_l':77,'foliar_completo_l':78,
   'dolomita':65,'cal_agricola':66,'asist_poscosecha':59,
   'modulos_poscosecha':60,'analisis_granos':64,'estimado':61,
   'reporte':62,'escoba':82,'carmenta':84,'moniliasis':81,
   'chinche':85,'pudricion':83,'sanos':79,'enfermos':80,
   'ctg':32,'eca':28,'parcela':29,'modulos':30,'dias':31,
   'hectareas':24,'comite_fitosanitario':26,'reuniones_actas':25,
   'metodologias_documento':27,
  }
  fila={c:0 for c in d.columns}
  for clave,indice_col in columnas.items():
   valor=pd.to_numeric(pd.Series([registro.iloc[indice_col]]),errors='coerce').iloc[0]
   valido=pd.notna(valor)
   v=float(valor) if valido else 0.0
   for sufijo,resultado in [('_sum',v),('_count',int(valido)),('_min',v)]:
    col=clave+sufijo
    if col in fila:fila[col]=resultado
   if clave in ('parcela','modulos','dias'):
    col=clave+'_nonempty'
    if col in fila:fila[col]=int(valido and v>0)
    if col+'_sum' in fila:fila[col+'_sum']=int(valido and v>0)
  for col,idx in [('ambito',2),('comunidad',11),('supervisor',3),
                  ('extensionista',6),('tecnico',7),('especialista_poscosecha',4)]:
   if col in fila:fila[col]=str(registro.iloc[idx]) if pd.notna(registro.iloc[idx]) else ''
  fila['participantes']=1
  d=pd.DataFrame([fila],columns=d.columns)
  st.caption("Vista individual desde el Excel privado.")

if d.empty:
 st.warning('No hay registros para la combinación de filtros seleccionada.')
st.sidebar.caption('Los nombres solo se leen del Excel cargado en esta sesión; no están en el CSV público.')
st.sidebar.info('Filtro mensual no disponible: Hoja 1 contiene acumulados, no una serie mensual verificable.')
def total(k):return float(d.get(k+'_sum',pd.Series(dtype=float)).sum())
def count(k):return float(d.get(k+'_count',pd.Series(dtype=float)).sum())
def avg(k):return total(k)/count(k) if count(k) else None
def minimum(k):
 x=d.loc[d.get(k+'_count',pd.Series(0,index=d.index))>0,k+'_min']
 return float(x.min()) if not x.empty else None
def display(v,dec=0):return 'Sin dato' if v is None else f'{v:,.{dec}f}'
def cards(items):
 for col,(label,k,mode,dec) in zip(st.columns(len(items)),items):
  v=total(k) if mode=='sum' else avg(k) if mode=='avg' else minimum(k) if mode=='min' else float(d[k].sum())
  col.metric(label,display(v,dec))
def bar(title,k,axis='comunidad',color=None,n=25):
 if d.empty:return
 a=d.groupby(axis,as_index=False)[k+'_sum'].sum().sort_values(k+'_sum',ascending=False).head(n)
 fig=px.bar(a,x=axis,y=k+'_sum',text_auto='.0f',title=title,color_discrete_sequence=[color] if color else None)
 fig.update_layout(height=430,xaxis_tickangle=-48,xaxis_title='',yaxis_title='',paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)',font=dict(size=13),title_font=dict(size=18,color='#0d365d'),margin=dict(t=65,b=85,l=15,r=12));fig.update_traces(marker_line_color='#ffffff',marker_line_width=1.5)
 st.plotly_chart(fig,width="stretch")
def icon_for(label):
 name=label.upper()
 if 'ESCOBA' in name or 'MONILIASIS' in name or 'PUDRICIÓN' in name:return '🍄'
 if 'CARMENTA' in name or 'CHINCHE' in name:return '🐞'
 if 'COMPOST' in name:return '🪴'
 if 'BIOFERMENT' in name or 'BIOFER.' in name or 'BIOFERTILIZ' in name:return '🛢️'
 if 'MÓDULO' in name:return '🏡'
 if 'PODA' in name:return '✂️'
 if 'MIP' in name:return '🐛'
 if 'ABON' in name:return '🌿'
 if 'HUMATO' in name:return '🧪'
 if 'POTASIO' in name or 'FOLIAR' in name or 'COBRE' in name or 'CALCIO' in name:return '🍃'
 if 'ASISTENCIA' in name:return '👩‍🌾'
 if 'PRODUCCIÓN' in name or 'GRANOS' in name or 'REPORTE' in name:return '🍫'
 if 'FRUTOS' in name:return '🍈'
 return '🌱'
def pale_hex(h):
 h=h.lstrip('#')
 if len(h)!=6:return '#f3f9ff'
 r,g,b=[int(h[i:i+2],16) for i in (0,2,4)]
 return '#%02x%02x%02x'%tuple(round(c*.12+255*.88) for c in (r,g,b))
def compact_card(label,value,color,subtitle='',dec=0):
 number=display(value,dec) if isinstance(value,(int,float)) else str(value)
 st.markdown(f"""<div class='compact-kpi' style='--accent:{color};--pale:{pale_hex(color)}'>
 <div class='compact-kpi-title'>{escape(label.upper())}</div>
 <div class='compact-kpi-value'>{escape(number)}</div>
 <div class='compact-kpi-note'>{escape(subtitle)}</div></div>""",unsafe_allow_html=True)

def target_card(label,value,target):
 pct=value/target*100 if target>0 else 0
 st.markdown(f"""<div class='cap-target-card' title='Meta oficial: {target:,.0f}'>
  <div class='cap-target-title'>{escape(label)}</div>
  <div class='cap-target-row'><span class='cap-target-value'>{escape(display(value))}</span><span class='cap-target-pct'>{pct:.1f} %</span></div>
 </div>""",unsafe_allow_html=True)

def community_breakdown(label,column,color):
 st.markdown(f"**{label}**")
 if column not in d.columns:
  st.info('Este indicador no está disponible en la base cargada.')
  return
 data=d.groupby('comunidad')[column].sum().sort_values(ascending=False)
 data=data[data>0]
 if data.empty:
  st.caption('Sin registros para los filtros seleccionados.')
  return
 st.caption(f'Total: {display(float(data.sum()))} · {len(data)} caseríos con registros')
 def draw(series):
  maximum=max(float(data.max()),1.0)
  for name,value in series.items():
   width=max(0,min(100,float(value)/maximum*100))
   st.markdown(f"<div class='community-row'><span>{escape(str(name))}</span><strong>{escape(display(float(value)))}</strong></div><div class='community-track'><div class='community-fill' style='width:{width:.2f}%;background:{color}'></div></div>",unsafe_allow_html=True)
 draw(data.head(5))
 if len(data)>5:
  with st.expander(f'Ver los {len(data)-5} caseríos restantes'):
   draw(data.iloc[5:])

def atp_top_communities():
 st.markdown('**Asistencia técnica personalizada por comunidad**')
 if d.empty:return
 a=d.groupby('comunidad')['atp_sum'].sum().sort_values(ascending=False)
 if a.empty:return
 top=a.head(5)
 fig=px.bar(x=top.values[::-1],y=top.index[::-1],orientation='h',text=top.values[::-1],color_discrete_sequence=['#e21b23'])
 fig.update_layout(height=260,margin=dict(t=10,b=20,l=8,r=30),xaxis_title='Asistencias',yaxis_title='',paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)',font=dict(size=12))
 fig.update_traces(textposition='outside',cliponaxis=False)
 st.plotly_chart(fig,width='stretch')
 if len(a)>5:
  with st.expander(f'Ver las {len(a)-5} comunidades restantes'):
   st.dataframe(a.iloc[5:].rename('Asistencias').reset_index().rename(columns={'comunidad':'Comunidad'}),hide_index=True,width='stretch')

def unique_field_days():
 # Un día de campo por extensionista con al menos un registro positivo.
 # La fuente está agregada por comunidad/técnico, pero conserva extensionista.
 if d.empty or 'dias_sum' not in d.columns:return 0
 active=d.loc[pd.to_numeric(d['dias_sum'],errors='coerce').fillna(0)>0,'extensionista']
 return int(active[active.astype(str).str.strip().ne('')].nunique())

def gauge(label,k,color,mode='sum',dec=0,advance=False,base=None,official_target=None):
 # Arco decorativo: no se interpreta como avance de una meta.
 v=total(k) if mode=='sum' else (avg(k)*100 if avg(k) is not None else None) if mode=='pct' else avg(k) if mode=='avg' else minimum(k) if mode=='min' else count(k)
 number=display(v,dec)+(' %' if mode=='pct' and v is not None else '')
 # ECA/CTG usan la meta oficial programada; ATP mantiene su base de hectáreas.
 if official_target is not None:
  denominator=float(official_target)
  pct=(v/denominator*100) if denominator>0 and v is not None else None
  badge=(f"<span class='devida-avance devida-avance-cap' title='Aporte a la meta oficial programada de {denominator:,.0f} asistencias'>{pct:,.1f} %</span>" if pct is not None else "<span class='devida-avance'>Sin base</span>")
 else:
  denominator=total(base) if advance and base else total('hectareas') if advance else 0
  pct=(v/denominator*100) if advance and denominator>0 and v is not None else None
  badge=(f"<span class='devida-avance' title='Avance sobre {denominator:,.2f} ha asignadas'>{pct:,.1f} %</span>" if pct is not None else "<span class='devida-avance'>Sin base</span>" if advance else "")
 # El valor queda centrado y completamente visible, incluso con miles.
 st.markdown(f"""<div class='devida-gauge-card' style='--gauge-color:{color};--gauge-pale:{pale_hex(color)}'>
   <div class='devida-gauge-title'>{escape(label.upper())}</div>
   <div class='devida-gauge-icon' aria-hidden='true'>{icon_for(label)}</div>
   <svg viewBox='0 0 350 160' role='img' aria-label='{escape(label)}: {escape(number)}'>
     <path d='M 44 133 A 131 131 0 0 1 306 133' fill='none' stroke='#e6ebef' stroke-width='23'/>
     <path d='M 44 133 A 131 131 0 0 1 175 2' fill='none' stroke='{color}' stroke-width='23'/>
     <text x='175' y='119' text-anchor='middle' font-family='Arial,sans-serif' font-size='{26 if len(number)>10 else 32}' font-weight='800' fill='#d71932'>{escape(number)}</text>
   </svg>
   {badge}
  </div>""",unsafe_allow_html=True)
def gauge_grid(items,cols=3,advance=False,stage_bases=False):
 for start in range(0,len(items),cols):
  row=items[start:start+cols]
  if len(row)==cols:
   slots=st.columns(cols,gap='small')
  elif len(row)==2 and cols==3:
   # Dos indicadores centrados en una fila de tres: simetría visual.
   slots=st.columns([0.5,1,1,0.5],gap='small')[1:3]
  elif len(row)==1 and cols==3:
   slots=st.columns([1,1,1],gap='small')[1:2]
  else:
   slots=st.columns(len(row),gap='small')
  for col,(label,key,color,mode,dec) in zip(slots,row):
   with col:
    gauge(label,key,color,mode,dec,advance=advance,base=('crecimiento_base' if key in ('abonamiento','poda_formacion','mip_crec') else 'produccion_base') if stage_bases else None)
T=st.tabs(['RESUMEN','CAPACITACIÓN','ATP','ABONOS ORG.','FOLIARES','POSCOSECHA','% FRUTOS'])
with T[0]:
 st.subheader('Resumen ejecutivo de la actividad cacao')
 with st.container(key='resumen_compacto'):
  c=st.columns(3)
  for x,(lab,k) in zip(c,[('🏘️ Comunidades atendidas','comunidad'),('👷 Supervisores','supervisor'),('👩‍🌾 Extensionistas','extensionista')]):x.metric(lab,d[k].nunique())
  c=st.columns(3);c[0].metric('👨‍👩‍👧‍👦 Participantes',f"{int(d['participantes'].sum()):,}");c[1].metric('🌱 Hectáreas asistidas',display(total('hectareas'),2));c[2].metric('🧑‍🔧 Técnicos',d['tecnico'].nunique())
 # Resumen compacto: valores reales del filtro, sin gráficos gigantes.
 c1,c2=st.columns(2,gap='small')
 with c1:compact_card('👨‍👩‍👧‍👦 Participantes por ámbito',int(d['participantes'].sum()),'#0877c9','Total de participantes del filtro')
 with c2:compact_card('🌱 Hectáreas por ámbito',total('hectareas'),'#16a34a','Superficie asistida del filtro (ha)',2)
 st.subheader('Gestión y organización comunitaria')
 r1,r2,r3=st.columns(3,gap='small')
 with r1:
  compact_card('COMITÉ FITOSANITARIO',total('comite_fitosanitario'),'#138c57','Registros del indicador')
  community_breakdown('Comité fitosanitario por caserío','comite_fitosanitario_sum','#138c57')
 with r2:
  compact_card('REUNIONES DE MOTIVACIÓN Y SOCIALIZACIÓN CON AUTORIDADES COMUNALES (ACTAS)',total('reuniones_actas'),'#0877c9','Actas registradas')
  community_breakdown('Actas por caserío','reuniones_actas_sum','#0877c9')
 with r3:
  compact_card('ORGANIZACIÓN DE LAS METODOLOGÍAS PARA EL SERVICIO DE EXTENSIÓN (DOCUMENTO)',total('metodologias_documento'),'#8755bc','Documentos registrados')
  community_breakdown('Documentos por caserío','metodologias_documento_sum','#8755bc')

with T[1]:
 st.subheader('Capacitación y extensión agraria')
 # CTG y ECA son asistencias acumuladas, no personas únicas.
 # Solo se conservan las tarjetas superiores de parcelas y módulos; ECA/CTG ya tienen sus medidores.
 c_par,c_mod=st.columns(2,gap='small')
 with c_par:target_card('Parcelas demostrativas',total('parcela_nonempty'),625)
 with c_mod:target_card('Módulos de innovación',total('modulos_nonempty'),625)
 # Metas oficiales mensuales: ECA 750 (extensionistas), CTG 1,823 (técnicos).
 # Marzo a noviembre = 9 meses programados. Porcentajes respecto a la meta global programada,
 # no metas individuales de los responsables ni recuentos de personas únicas.
 MESES_PROGRAMADOS=9
 META_ECA=750*MESES_PROGRAMADOS
 META_CTG=1823*MESES_PROGRAMADOS
 c1,c2=st.columns(2,gap='small')
 with c1:gauge('ECA · ASISTENCIAS','eca','#d7b900',dec=0,official_target=META_ECA)
 with c2:gauge('CTG · ASISTENCIAS','ctg','#0877c9',dec=0,official_target=META_CTG)
 st.caption(f'ECA (extensionistas): meta oficial programada {META_ECA:,} asistencias. CTG (técnicos): meta oficial programada {META_CTG:,} asistencias. Cada porcentaje indica la contribución del filtro seleccionado a la meta global de marzo a noviembre; no es una meta individual.')
 c1,c2,c3=st.columns(3,gap='small')
 with c1:compact_card('🌱 Días de campo',unique_field_days(),'#d97706','Máximo uno por extensionista en el año')
 with c2:gauge('Módulos de innovación','modulos_nonempty','#ff006e')
 with c3:gauge('Parcelas demostrativas','parcela_nonempty','#35d71d')
 st.caption('Días de campo: número de extensionistas con al menos un registro positivo, independientemente de cuántos participantes hayan registrado. ECA y CTG: asistencias acumuladas.')
with T[2]:
 st.subheader('Asistencia técnica: crecimiento y producción')
 c1,c2=st.columns([2,1])
 with c1:atp_top_communities()
 with c2:
  st.metric('FAMILIAS ATENDIDAS',display(float(d['participantes'].sum())))
  st.metric('ATP',display(total('atp')))
 gauge_grid([
  ('PODA MANT. (HAS)','poda_mantenimiento','#104f94','sum',2),
  ('MIP - PRODUCCIÓN (HAS)','mip_prod','#18d4e5','sum',2),
  ('APLIC. BIOFER. (HAS)','aplic_biofert','#f0001c','sum',2),
  ('ABONAMIENTO - CRECIMIENTO (HAS)','abonamiento','#a83b43','sum',0),
  ('PODA FORMACIÓN - CRECIMIENTO (HAS)','poda_formacion','#00d83c','sum',0),
  ('MIP - CRECIMIENTO (HAS)','mip_crec','#12cde4','sum',0),
  ('ABON. FRUCTIFICAC. (HAS)','abon_fructificacion','#ff870a','sum',0),
  ('ABON. BOTÓN FLORAL (HAS)','abon_boton','#05c934','sum',0),
  ('ABON. FLORACIÓN (HAS)','abon_floracion','#cccccc','sum',0)
 ],cols=3,advance=True,stage_bases=True)
 st.caption('Avance (%) = hectáreas ejecutadas ÷ superficie registrada de la etapa correspondiente (crecimiento o producción) × 100. Los valores pueden superar 100 % por intervenciones repetidas; no equivalen necesariamente a cumplimiento de metas.')
with T[3]:
 st.subheader('Producción de abonos orgánicos')
 gauge_grid([
  ('Mantenimiento módulos biofermentos','mant_biofermentos','#593c99','sum',0),
  ('Producción compost (kg)','compost_producido_kg','#75371e','sum',0),
  ('Producción biofermentos (L)','biofermentos_producidos_l','#f2ef00','sum',0),
  ('Aplicación biofertilizantes (L)','biofertilizantes_aplicados_l','#fa0022','sum',0)
 ],cols=2)
with T[4]:
 st.subheader('Asistencia técnica: otras actividades')
 gauge_grid([
  ('Humato de potasio (L)','humato_l','#111111','sum',0),
  ('Sulfopotásico (L)','sulfopotasico_l','#ffff00','sum',1),
  ('Cobre quelatado (L)','cobre_quelatado_l','#101e64','sum',1),
  ('Fosfito de potasio (L)','fosfito_potasio_l','#ff8512','sum',0),
  ('Calcio-boro-zinc (L)','foliar_cbz_l','#04d4ef','sum',0),
  ('Foliar PK (L)','foliar_pk_l','#5720ff','sum',1)
 ],cols=3)
 st.caption('Indicadores adicionales del filtro seleccionado')
 gauge_grid([
   ('ACODOS AÉREOS','acodos','#32b86a','sum',0),
   ('APLICACIÓN DOLOMITA (KG)','dolomita','#8755bc','sum',0),
   ('APLICACIÓN CAL AGRÍCOLA (KG)','cal_agricola','#ed9218','sum',0)
 ],cols=3)
with T[5]:
 st.subheader('Cosecha y poscosecha')
 gauge_grid([
  ('Asistencia técnica','asist_poscosecha','#ffff00','sum',0),
  ('Mantenimiento de módulos','modulos_poscosecha','#ff8a00','sum',0),
  ('Análisis físico de granos','analisis_granos','#8835a1','sum',0),
  ('Estimado de producción · promedio','estimado','#00d732','avg',0),
  ('Reporte de producción · promedio','reporte','#ff0024','avg',0)
 ],cols=3)
 st.caption('Estimado y reporte de producción: promedios de registros válidos, redondeados para la visualización.')
with T[6]:
 st.subheader('Evaluación de plagas y frutos')
 # Valores originales: fracciones (0.019 = 1.90 %); se muestran como porcentaje.
 gauge_grid([
  ('ESCOBA DE BRUJA %','escoba','#6cb5ff','pct',2),
  ('CARMENTA %','carmenta','#20e92b','pct',2),
  ('MONILIASIS %','moniliasis','#69df00','pct',2),
  ('CHINCHE %','chinche','#9a7ae0','pct',2),
  ('PUDRICIÓN PARDA %','pudricion','#76232c','pct',2)
 ],cols=3)
 san,enf=avg('sanos'),avg('enfermos')
 if san is not None and enf is not None:
  # Source percentage columns are stored as percentages (not proportions).
  a=pd.DataFrame({'Estado':['Sanos','Enfermos'],'Porcentaje':[san,enf]})
  fig=px.pie(a,names='Estado',values='Porcentaje',hole=.6,title='Porcentaje de frutos sanos y enfermos',color='Estado',color_discrete_map={'Sanos':'#0a548f','Enfermos':'#e21b23'})
  fig.update_traces(textinfo='percent+label',texttemplate='%{label}: %{percent:.2%}',marker=dict(line=dict(color='white',width=3)),pull=[0,.04]);fig.update_layout(height=500,paper_bgcolor='rgba(0,0,0,0)',font=dict(size=15))
  st.plotly_chart(fig,width="stretch")
 else:st.info('No hay porcentajes de frutos válidos para esta selección.')
 st.caption('Incidencia de plagas: promedio de registros válidos × 100. Frutos sanos y enfermos: porcentajes originales utilizados para el gráfico.')
st.divider();st.caption('Datos agregados para uso de validación. No publicar el Excel original ni información personal de productores. Verificar autorización institucional antes de difundir.')
