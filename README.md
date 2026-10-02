# Ejercicio 3.1.4 — LM Studio + Python

## 1. Objetivo

En este ejercicio conecto Python con un modelo de lenguaje ejecutándose localmente en LM Studio. La idea es comprobar cómo responde ante un prompt correcto y otro con errores.

## 2. Configuración

He utilizado Python, `uv`, OpenAI SDK, LM Studio y Qwen3-8B.

LM Studio funciona como servidor local en `http://localhost:1234/v1`.

Desde Python me conecto utilizando el SDK de OpenAI.

## 3. Prueba

Para la prueba he utilizado un texto sobre Virtual Cell, un proyecto de simulación celular desarrollado con Python.

He enviado dos prompts. El primero está escrito de forma clara y sin errores. El segundo contiene faltas de ortografía y una estructura más informal.

## 4. Resultado

Qwen3-8B ha comprendido correctamente los dos prompts y ha generado respuestas coherentes y muy similares.

Aunque el segundo prompt tenía errores como `celula`, `mas` y `programacion`, el modelo ha podido entender la intención y resumir correctamente el contenido.

## 5. Conclusión

En esta prueba los errores no han impedido que el modelo comprenda la petición. Esto muestra que Qwen3-8B puede tolerar ciertos errores de escritura cuando el significado general del mensaje sigue siendo claro.
