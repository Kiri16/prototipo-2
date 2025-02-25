from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculadora', methods=['POST', 'GET'])
def calculadora():
    if request.method == 'POST':
        peso = float(request.form['peso'])
        altura = float(request.form['altura'])
    elif request.method == 'GET':
        peso = float(request.args.get('peso'))
        altura = float(request.args.get('altura'))

    imc = peso / (altura ** 2)
    
    if imc < 18.5:
        img = 'underweight.png'   #imagenes
        diagnostico = 'Bajo peso'
        explanation = 'El resultado sugiere que tienes bajo peso. Es posible que necesites aumentar tu ingesta calórica.'
        aviso = 'Consulta con un nutricionista para una dieta adecuada y equilibrada que te ayude a alcanzar un peso saludable.'
    elif 18.5 <= imc < 24.9:
        img = 'normal.png'
        diagnostico = 'Peso normal'
        explanation = 'El resultado indica que tienes un peso saludable en relación con tu altura. ¡Sigue así!'
        aviso = 'Continúa con tu estilo de vida saludable, manteniendo una dieta equilibrada y realizando ejercicio regularmente.'
    elif 25 <= imc < 29.9:
        img = 'overweight.png'
        diagnostico = 'Sobrepeso'
        explanation = 'El resultado sugiere que tienes sobrepeso. Puede ser beneficioso reducir la ingesta calórica y aumentar la actividad física.'
        aviso = 'Considera aumentar tu actividad física y vigilar tu dieta para alcanzar un peso más saludable.'
    else:
        img = 'obese.png'
        diagnostico = 'Obesidad'
        explanation = 'El resultado indica que tienes obesidad. Es importante buscar asesoría médica para gestionar tu peso de manera efectiva.'
        aviso = 'Es recomendable buscar asesoría médica y nutricional para un plan integral que te ayude a reducir el peso.'
        
    return render_template('result.html', imc=imc, img=img, diagnostico=diagnostico, explanation=explanation, aviso=aviso)

@app.route('/diagnostico/<diagnostico>')
def diagnostico_page(diagnostico):
    avisos = {
        'Bajo peso': 'Consulta con un nutricionista para una dieta adecuada.',
        'Peso normal': 'Continúa con tu estilo de vida saludable.',
        'Sobrepeso': 'Considera aumentar tu actividad física y vigilar tu dieta.',
        'Obesidad': 'Es recomendable buscar asesoría médica y nutricional.'
    }
    
    return render_template('diagnostico.html', diagnostico=diagnostico, aviso=avisos[diagnostico])

if __name__ == '__main__':
    app.run(debug=True)
