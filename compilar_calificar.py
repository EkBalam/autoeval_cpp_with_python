import os
import subprocess
import json
import pandas as pd

from sys import platform
if platform == "linux" or platform == "linux2" or  platform == "darwin":
    EXT = "out"
elif platform == "win32":
    EXT = "exe"

def compile(filename):
    result = subprocess.run(
        ["g++", filename], capture_output=True, text=True
    )
    if result.stderr:
        return result.stderr
    return "compiled"
    

if __name__ == "__main__":
    data = pd.read_csv('alumnos.csv')
    repos = ['p09-funciones-y-procedimientos-', 'ps-12-tablero-recursivo-', 'ps13-buscaminas-', 'ps14-q-learning-', 'p14-archivos-de-texto-']
    resultados = []
    for index, row in data.iterrows():
        alumno = (row['nombre']+row['apellido']).replace(" ", "_")
        print(alumno)
        resultado = {}
        resultado['alumno'] = alumno
        for repo_o in repos:
            repo = repo_o+row['usuario']
            folder = f'tareas_tercer_parcial/{alumno}/{repo}'
            list = []
            compilados = 0
            for (root, dirs, file) in os.walk(folder):
                for f in file:
                    if '.cpp' in f:
                        list.append(f)
                        compilado = compile(folder+'/'+f)
                        print('\t',folder, f, compilado)
                        if compilado == 'compiled':
                            compilados += 1
            resultado[repo_o+'_leidos']  = len(list)
            resultado[repo_o+'_compilados']  = compilados
        resultados.append(resultado)
        #break
    res = pd.DataFrame.from_dict(resultados)
    res.to_csv('tareas_compiladas_3_parcial.csv')
