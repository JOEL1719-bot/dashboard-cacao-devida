# Dashboard Cacao — filtros de ámbito y comunidad

Actualización del prototipo público. Se incorporan filtros desplegables «Todos» por ámbito y comunidad, relacionados entre sí. Las comunidades con menos de 10 registros se agregan bajo «OTRAS COMUNIDADES (AGRUPADAS)».

**No son cifras oficiales validadas:** los registros pueden diferir de familias únicas y las sumas no se han conciliado con DAX. No existe desglose mensual validado en la hoja de productores.

**Seguridad:** No subir el Excel original ni el PBIX. Este CSV solo incluye sumas agregadas por ámbito/comunidad, pero antes de divulgarlo como institucional debe existir autorización. El filtro por personal no se incluye porque revelaría nombres o combinaciones potencialmente identificables.

Para actualizar GitHub, reemplazar `app.py` y añadir `datos_publicos_comunidad.csv` en el mismo repositorio. Mantener `requirements.txt` existente.
