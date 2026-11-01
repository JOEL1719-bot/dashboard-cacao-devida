# Dashboard Cacao — corrección de hectáreas (versión de validación)

**Corrección:** la tarjeta y el gráfico de hectáreas del RESUMEN ahora usan la suma de `TOTAL` (columna V de Hoja 1), que es el campo referenciado por el gráfico «HECTÁREAS ASISTIDAS POR ÁMBITO» del PBIX original. Antes se utilizaba «Hectáreas Asistidas (a+b)» (columna Y), que corresponde a otro indicador.

Para el técnico Aderson Estacio, el cálculo corregido debe mostrar 109.00 ha y 65 familias (con el resto de filtros en Todos), frente a 88.83 ha antes. El corte del Excel es octubre de 2026, pero el filtro MES REPORTADO del PBIX aparece en JUNIO en la captura; comparar otros indicadores requiere conciliar ese contexto.

Esta versión no modifica las siete pestañas, el diseño ni los cinco filtros. No se ha validado aún la totalidad de medidas de Power BI, ni se ha implementado el filtro mensual. La aplicación es pública y muestra nombre y primer apellido del personal: mantener autorización institucional. No subir el Excel ni el PBIX.

En GitHub, reemplazar `app.py` y `datos_publicos_personal.csv` (opcionalmente README.md). Mantener `requirements.txt`.
