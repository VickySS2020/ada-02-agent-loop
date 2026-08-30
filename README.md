# Preguntas obligatorias
## ¿Qué es tool calling?
Mecanismo mediante el cual un modelo puede solicitar la ejecución de una herramienta basado en las indicaciones del usuario y su contexto.

## ¿Qué es una observation?
Es aquella información que el agente descubre después de ejecutar una acción y que es usada en los pasos subsecuentes que toma el agente.

## ¿Qué es el Agent Loop?
Es el ciclo de razonamiento y acción que permite que el agente trabaje iterativamente, basándose en el siguiente principio: invocar el modelo, checar si desea usar una herramienta, ejecutarla, retroalimentar el resultado al modelo para otra ronda de razonamiento; y todo este proceso se repite hasta que el modelo proporcione una respuesta final o hasta que se haya completado la tarea.

## ¿Qué operaciones corresponden a read, write, edit y bash?
- Read: Leer los contenidos de un archivo.
- Write: Crear un nuevo archivo o reemplazar completamente el contenido de uno existente.
- Edit: Modificar ciertas partes de un archivo existente.
- Bash: Correr comandos en la terminal en el entorno de trabajo.

## ¿Dónde intervino el agente?
En la corrección del error en una de las pruebas de test_calculator.py y en la adición de la nueva función modulo() que saca el residuo entre 2 números. Igualmente, ejecutó las pruebas antes y después de cada implementación.

## ¿Dónde intervino el humano?
El usuario tuvo que proporcionar al agente con la información necesaria para trabajar en el proyecto (código fuente del programa y pruebas), verificar los cambios realizados a ciertas partes del código antes de que estos fueran implementados en el entorno de proyecto, y dar permiso al agente de IA para ejecutar comandos en la terminal.

## ¿Qué capacidad se perdería sin ejecución de comandos?
El agente no sería capaz de ejecutar las pruebas del documento test_calculator.py, y por lo tanto, no podría verificar errores en la calculadora o verificar que los cambios que realizó hayan funcionado.