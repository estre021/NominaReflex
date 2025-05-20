
#  NOMINAREFLEX - Calculadora de Nómina en Reflex

**NOMINAREFLEX** es una aplicación web desarrollada con [Reflex](https://reflex.dev), pensada para calcular de manera precisa el sueldo neto de un empleado en la República Dominicana. Esta herramienta aplica correctamente los descuentos de la TSS, el ISR y contempla bonificaciones y otros ajustes relevantes.
NOMINAREFLEX/
├── .env/                 # Entorno virtual
├── .states/              # Estados administrados por Reflex
├── .web/                 # Archivos generados automáticamente
├── assets/               # Archivos estáticos como imágenes o íconos
├── NominaReflex/         # Lógica central de la aplicación
│   ├── __init__.py
│   ├── NominaReflex.py   # Página principal de la aplicación
│   └── state.py          # Lógica de negocio y estado (cálculos)
├── .gitignore
├── README.md             # Documentación del proyecto
├── requirements.txt      # Lista de dependencias
└── rxconfig.py           # Configuración del proyecto Reflex
```

---

## Cómo Clonar y Ejecutar el Proyecto

### 1. Clona el repositorio

```bash
git clone https://github.com/estre021/NominaReflex.git
cd NominaReflex
```

### 2. Crea un entorno virtual (opcional pero recomendado)

```bash
python -m venv .env
source .env/bin/activate  # En Windows: .env\Scripts\activate
```

### 3. Instala Reflex y dependencias

```bash
pip install reflex
pip install -r requirements.txt
```

### 4. Ejecuta la app

```bash
reflex run
```

👉 Luego, abre tu navegador y visita: [http://localhost:3000](http://localhost:3000)

---

