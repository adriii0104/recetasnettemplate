from flask import Flask, render_template, request, redirect, url_for
from FUNC import config

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        from APIREQUESTS import apirest
        name = request.form.get('name').title()
        username = request.form.get('username').lower()
        email = request.form.get('email').lower()
        is_chief = True if request.form.get('is_chief') == 'on' else False

        password = config.hash_password(request.form.get('password'))

        user_id = apirest.API_REGISTER(name, username, email, is_chief, password)

        if user_id == 100:
            return redirect(url_for('index'))
        elif user_id:
            return redirect(f'/success/{user_id}')
        else:
            return redirect(url_for('index'))
    
    return render_template(config.routes_patches['INICIO'])



@app.route('/success/<value>', methods=['GET'])
def success(value):
    from APIREQUESTS import apirest

    results = apirest.token_verify(value)

    if results:
        return render_template(config.routes_patches['REGISTRO_EXITOSO'])
    
    else: return 'El token es invalido o ya venció.'



if __name__ == "__main__":
    app.run(debug=True)
