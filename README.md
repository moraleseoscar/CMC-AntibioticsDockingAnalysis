
# CMC-Antibiotics_Docking_Analysis

Este repositorio contiene los scripts y archivos necesarios para realizar el modelado computacional, optimización geométrica y simulación de interacciones entre el carboximetil quitosano (CMC) y varios antibióticos (diclofenaco, ibuprofeno, triclosán y dexketoprofeno). Estos procedimientos están diseñados para evaluar el potencial del CMC como material adsorbente en la remediación de contaminantes emergentes en cuerpos de agua.

## Estructura del Repositorio

La estructura del repositorio es la siguiente:

```
CMC-Antibiotics_Docking_Analysis/
├── CMC/
├── Complejos/
│   ├── CMC-Diclofenac/
│   │   ├── CMC-Diclofenac_OrcaFiles/
│   │   ├── Complejo_CMCdiclofenac.inp
│   │   └── ...
│   └── ...
├── Ibuprofeno/
│   ├── Ibuprofen_B3LYP_6-311+G/
│   ├── Ibuprofen_B3LYP_STO-3G/
│   └── ...
├── Dexketoprofeno/
├── Triclosan/
├── 1Generate_orcainp.py
├── 2Run_orca.py
├── 3Modificate_xyzfile.py
├── 4Generate_outfiles_to_spect.py
├── 5Orca_mapsABS.py
├── 6RunComplex.py
├── Generate_graphs.ipynb
└── README.md
```

Cada antibiótico cuenta con subcarpetas que contienen archivos generados en el proceso de optimización y simulación, incluyendo archivos `.xyz`, `.gbw`, y `.out` para el análisis de resultados y cálculo de energía de unión. Además, en cada carpeta se encuentran las configuraciones correspondientes de bases y funcionales para cada cálculo.


## Requisitos

Para ejecutar los scripts y realizar las simulaciones es necesario tener instalados los siguientes programas:

- **Python** (versión 3.8 o superior)
- **ORCA** (versión 5.0 o superior para cálculos cuánticos)
- **Open Babel** (versión 3.1.1 o superior para la conversión de archivos)
- **AutoDock Vina** (versión 1.2.5 o superior para el docking molecular en Chimera)
- **Chimera** (versión 1.18 o superior para visualización y preparación de estructuras)

Además, algunas librerías de Python, como `pandas`, `matplotlib`, `os`, y `subprocess`, son requeridas para la ejecución de los scripts.

## Descripción de los Scripts

### 1. `1Generate_orcainp.py`

Este script genera los archivos de entrada para ORCA en formato `.orcainp` a partir de las secuencias SMILES de los antibióticos. Especifica las bases y funcionales a probar.

**Uso:**
```bash
python 1Generate_orcainp.py <nombre> <secuencia>
```

**Ejemplo:**
```bash
python 1Generate_orcainp.py diclofenac "C14H10Cl2NO2"
```

### 2. `2Run_orca.py`

Ejecuta los cálculos de ORCA para cada combinación de funcional y base especificada en los archivos de entrada.

**Uso:**
```bash
python 2Run_orca.py <nombre>
```

**Ejemplo:**
```bash
python 2Run_orca.py diclofenac
```

### 3. `3Modificate_xyzfile.py`

Modifica los archivos `.xyz` generados y ajusta el formato de entrada para ORCA. 

**Uso:**
```bash
python 3Modificate_xyzfile.py <directorio>
```

### 4. `4Generate_outfiles_to_spect.py`

Genera los archivos de salida necesarios para el análisis espectroscópico desde los archivos de entrada `.xyz`.

**Uso:**
```bash
python 4Generate_outfiles_to_spect.py <nombre>
```

### 5. `5Orca_mapsABS.py`

Este script utiliza ORCA para generar los archivos `.abs` para análisis espectroscópico a partir de los archivos `.out`.

**Uso:**
```bash
python 5Orca_mapsABS.py <Carpeta>
```

### 6. `6RunComplex.py`

Ejecuta el cálculo final de energía de unión entre CMC y cada antibiótico en complejos optimizados.

**Uso:**
```bash
python 6RunComplex.py <directorio de complejos>
```

### 7. `Generate_graphs.ipynb`

Este Jupyter Notebook contiene el código necesario para graficar y analizar los espectros de absorción generados. Se utiliza `matplotlib` para visualizar las comparaciones entre los espectros computacionales y experimentales.


## Notas

- Todos los scripts deben ejecutarse en el orden especificado para completar correctamente el pipeline de simulación y análisis.
- Asegúrate de configurar las rutas y nombres de archivo en cada script de acuerdo con la estructura de directorios de tu sistema.


## Créditos

Este trabajo se ha desarrollado con el apoyo del Pueblo Americano a través de la Agencia de los Estados Unidos para el Desarrollo Internacional (USAID), bajo el acuerdo cooperativo número 7200AA21CA00009 del programa ASPIRE.