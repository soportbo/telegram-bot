import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generar_itinerario(datos_usuario):
    prompt = f"""
Eres un experto en turismo. Genera un itinerario para un viaje con los siguientes datos:
- Destino: {datos_usuario['destino']}
- Fechas: {datos_usuario['fechas']}
- Alojamiento: {datos_usuario['direccion']}
- Transporte: {datos_usuario['transporte']}
- Intereses: {datos_usuario['intereses']}
- Tipo de paseos: {datos_usuario['paseos']}

El itinerario debe tener:
- Actividades cercanas al alojamiento (hasta 15 cuadras).
- Actividades accesibles en transporte (gratis y con costo).
- Ordenado por día.
- Usar un lenguaje claro y motivador.
"""

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )

    return response.choices[0].message.content
