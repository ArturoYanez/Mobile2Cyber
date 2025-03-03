# 🚀 Mobile2Cyber - Programación Resiliente desde un Móvil  

**Objetivo**: Demostrar que se puede desarrollar software profesional SIN LAPTOP, usando solo un smartphone Android.  

## 🔥 Último Breakthrough  
> *"Corregí un error crítico causado por un typo usando solo flake8 en Termux"*  
> [Ver video](https://vm.tiktok.com/ZMBJCM6fG/) | [Ver configuración anti-errores](.flake8)  

## 🛠️ Configuraciones Clave  
1. **NeoVim para Móvil**: Optimizado para 2GB RAM [Guía aquí](nvim/README.md)  
2. **Alias de Productividad**: `lint`, `backup`, `organize` [Ver scripts](termux-setup/)  
3. **Flujo PEP8**: Detección de typos/errores en tiempo real [Demo](video-resources/flake8-alias-demo.gif)

### **Flake8: Linting Profesional en Móvil**  
¡Detecta typos y errores de estilo *antes de commitear*!  

#### **Uso Básico:**  
```bash  
# Analizar todo el proyecto
flake8 .

# Analizar un archivo específico
flake8 src/script.py

# Ejemolo de salida
src/script.py:5:1: E302 expected 2 blank lines, found 1  
src/script.py:10:80: E501 line too long (89 > 88 characters)
```

#### **Configuración Móvil-Optimizada:**  
- **`max-line-length = 88`**: Límite flexible para pantallas pequeñas.  
- **`exclude = .git, __pycache__`**: Ignora archivos no relevantes.  
- **`ignore = E203, W503`**: Reglas flexibles para desarrollo ágil.  

[Ver archivo .flake8 completo](.flake8) | [Demo en TikTok](video-resources/flake8-alias-demo.gif)  

___

## 🌱 Roadmap Público  
| **Hito**                     | **Progreso** | **Sponsors Necesarios** |  
|------------------------------|--------------|-------------------------|  
| Lanzar PyPI 0.1.0            | 90%          | 2/5 alcanzados          |  
| Script de escaneo ARP        | 10%          | 0/3                     |  
| App móvil para pentesting    | 0%           | Necesitamos 10 sponsors |  

[💪 Únete como Sponsor](https://github.com/sponsors/ArturoYanez)  

## 📌 Cómo Usar Este Repo  
1. Clona el repo:  
   ```bash  
   git clone https://github.com/ArturoYanez/Mobile2Cyber.git  
