import pandas as pd
import git  # pip install gitpython


repos = ['p09-funciones-y-procedimientos-', 'ps-12-tablero-recursivo-', 'ps13-buscaminas-', 'p14-archivos-de-texto-', 'ps14-q-learning-']
git_name = 'balamacademy'
data = pd.read_csv('alumnos.csv')

for index, row in data.iterrows():
    alumno = (row['nombre']+row['apellido']).replace(" ", "_")
    
    for repo in repos:
        repo = repo+row['usuario']
        try:
            git.Repo.clone_from(f'https://github.com/{git_name}/{repo}', f'tareas_tercer_parcial/{alumno}/{repo}')
        except Exception as e:
            print(e)
