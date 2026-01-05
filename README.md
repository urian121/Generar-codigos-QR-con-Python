## 🚀 Paso 1: Crear el entorno virtual

```bash
python3 -m venv env
```

## ⚡ Paso 2: Activar el entorno virtual

**Windows**

```bash
env\Scripts\activate
```

**macOS / Linux**

```bash
source env/bin/activate
```

## 📦 Paso 3: Instalar dependencias

```bash
pip install flask qrcode pillow
```

* **Flask** → framework web
* **qrcode** → genera códigos QR
* **Pillow** → manejo de imágenes (indispensable para QR)

## 📋 Paso 4: Ver paquetes instalados

```bash
pip list
# o
pip freeze
```

## 🧾 Paso 5: Crear / actualizar `requirements.txt`

```bash
pip freeze > requirements.txt
```

👉 Para correr el proyecto en otro equipo:

```bash
pip install -r requirements.txt
```

(Listo, magia negra controlada 😄)

## 🔌 Desactivar el entorno virtual

```bash
deactivate
```

## 🔄 Actualizar pip

```bash
python -m pip install --upgrade pip
```

## 📚 Referencia

🔗 [https://pypi.org/project/qrcode/](https://pypi.org/project/qrcode/)

Si quieres, te lo dejo en formato **README.md** o lo adaptamos a **Django / FastAPI** 👀
