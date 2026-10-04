# 🏥 Aplicación Hospital — Base de datos PostgreSQL

Proyecto de **administración de bases de datos** del ciclo ASIX: diseño, seguridad y alta disponibilidad de la base de datos de un hospital (`hospital_blanes`), con una aplicación de escritorio en Python para usarla.

![Panel de la aplicación](screenshots/panel.png)

## Qué incluye

| Bloque | Contenido |
| --- | --- |
| [Diseño ER y modelo relacional](Disseny%20ER%20-%20Model%20Relacional) | Modelo entidad-relación, modelo relacional y scripts SQL de tablas, roles y permisos. |
| [Conectividad y login](Bloc%20de%20connectivitat%20i%20login) | Aplicación Tkinter con inicio de sesión, registro con aprobación, roles y registro de accesos. |
| [Consultas](Bloc%20de%20consultes) | Historial de pacientes, agenda de médicos, quirófanos, informes por planta e índices de rendimiento. |
| [Exportación de datos](Bloc%20d'exportació%20de%20dades) | Exportación de resultados a XML y JSON. |
| [Dummy Data](Dummy%20Data) | Generación de 50.000 pacientes y 100.000 visitas con Faker para pruebas de carga. |
| [Esquema de seguridad](Esquema%20de%20Seguretat) | Matriz de roles (mínimo privilegio), *data masking*, SSL y auditoría según el RGPD. |
| [Alta disponibilidad](Esquema%20Alta%20Disponibilitat) | Réplica en la nube por VPN, RAID 10 con LVM, copias de seguridad y restauración. |

La documentación de cada bloque está en catalán.

## Tecnologías

PostgreSQL · SQL · Python · Tkinter · psycopg2 · Werkzeug (hash de contraseñas) · Faker

## Seguridad aplicada

- Contraseñas guardadas con hash, nunca en texto plano.
- Cuatro roles con permisos mínimos: `dba`, `metge`, `infermer` y `administratiu`.
- Enmascaramiento de datos personales para los roles que no necesitan verlos.
- Conexión cifrada con SSL y registro de accesos.

## Cómo ejecutarlo

1. Crea la base de datos con los scripts de `Disseny ER - Model Relacional`.
2. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```
3. Copia `Bloc de connectivitat i login/settings.example.json` a `settings.json` en la misma carpeta y pon tus datos de conexión. Ese archivo no se sube al repositorio.
4. Inicia la aplicación:
   ```
   cd "Bloc de connectivitat i login"
   python app.py
   ```

## Capturas

| Inicio de sesión | Administración | Registro de accesos |
| --- | --- | --- |
| ![Registro](screenshots/reg.png) | ![Administración](screenshots/admin.png) | ![Logs](screenshots/logs.png) |

---

Autor: [Pau Alarcón](https://paualarcon.com) · [LinkedIn](https://www.linkedin.com/in/pau-alarcon-ruiz-4a1424437/)
