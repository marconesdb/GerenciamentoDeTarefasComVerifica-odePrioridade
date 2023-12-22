from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista de tarefas em memória
tasks = []

@app.route('/')
def index():
    # Ordena as tarefas por prioridade antes de exibi-las
    sorted_tasks = sorted(tasks, key=lambda x: x['priority'])
    return render_template('index.html', tasks=sorted_tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    description = request.form.get('description')
    date = request.form.get('date')
    priority = int(request.form.get('priority'))

    # Validando prioridade
    if not 1 <= priority <= 5:
        return "Prioridade inválida. Deve estar entre 1 e 5."

    task = {'description': description, 'date': date, 'priority': priority}
    tasks.append(task)

    return redirect(url_for('index'))

@app.route('/update_task/<int:index>', methods=['GET', 'POST'])
def update_task(index):
    if request.method == 'GET':
        task = tasks[index]
        return render_template('update_task.html', index=index, task=task)
    elif request.method == 'POST':
        description = request.form.get('description')
        date = request.form.get('date')
        priority = int(request.form.get('priority'))

        # Validando prioridade
        if not 1 <= priority <= 5:
            return "Prioridade inválida. Deve estar entre 1 e 5."

        tasks[index] = {'description': description, 'date': date, 'priority': priority}
        return redirect(url_for('index'))

@app.route('/delete_task/<int:index>')
def delete_task(index):
    del tasks[index]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
