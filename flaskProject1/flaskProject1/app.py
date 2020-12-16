from flask import Flask, json, request

app = Flask(__name__)


@app.route('/1', methods=['GET'] )
def tela1():
    return 'Clique para Cadastrar'

@app.route('/2', methods=['GET'])
def tela2():
    return 'Preencha os campos a seguir' 

@app.route('/3', methods=['POST'] )
def feedback(self):
    feedback = self.request.get('feedback')
    self.response.out.write(feedback)       

if __name__ == '__main__':
    app.run()
