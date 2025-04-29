from flask import Flask, request, make_response, redirect #, render_template

app = Flask(__name__)

@app.route('/index')
def index():
    #return render_template('index.html')
    user_ip_info = request.remote_addr
    response = make_response(redirect("/show_info_address"))

    response.set_cookie("user_ip_information", user_ip_info)
    return response
    #return f"Tu direccion IP es: {user_ip_info}"

# Tambien funciona con solo app.run()
if __name__ == '__main__':
    app.run(debug=True) # En entornos de producción el debug=True se va, porque revela el back al cliente,
                        # y eso es un error de seguridad.