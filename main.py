from openai import OpenAI


client = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio",
)

MODEL = "qwen3-8b"


def get_completion(prompt: str, temperature: float = 0):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "Eres un asistente en español y respondes "
                    "con la mayor exactitud posible."
                ),
            },
            {"role": "user", "content": prompt},
        ],
        temperature=temperature,
    )

    return response.choices[0].message.content


def main():
    prompt_correcto = """
Lee el siguiente texto y resume su contenido en 3 puntos breves:

Virtual Cell es un proyecto de simulación de una célula viva mediante Python.
El objetivo es construir un modelo computacional que permita representar
algunos de los procesos que ocurren dentro de una célula y estudiar cómo
interactúan entre sí. El proyecto comienza con una bacteria como organismo
sencillo y, progresivamente, incorpora elementos como el metabolismo,
el entorno y los cambios en el estado de la célula. La intención es combinar
programación, biología y modelos matemáticos para crear una representación
computacional del comportamiento celular.
"""

    prompt_con_errores = """
lee el texto y haz un resumen en 3 puntos cortos

Virtual Cell es un proyecto para simular una celula viva usando Python.
La idea es representar procesos que pasan dentro de una celula y como
se relacionan entre ellos. El proyecto empieza con una bacteria porque
es mas sencilla y poco a poco añade metabolismo, entorno y cambios del
estado de la celula. Se quiere juntar programacion biologia y matematicas
para hacer una representacion en ordenador de como funciona una celula.
"""

    print(" PROMPT CORRECTO ")
    print(get_completion(prompt_correcto))

    print("\n PROMPT CON ERRORES ")
    print(get_completion(prompt_con_errores))


if __name__ == "__main__":
    main()
