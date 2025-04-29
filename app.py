from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)

@app.route('/index')
def index():
    #return render_template('index.html')
    user_ip_information = request.remote_addr    # Obtiene la dirección del cliente            

    response = make_response(redirect("/show_information_address"))  # Crea una respuesta y la redirecciona a otra url

    response.set_cookie("user_ip_information", user_ip_information) # Crea una cookie
    return response
    #return f"Tu direccion IP es: {user_ip_info}"

@app.route("/show_information_address")
def show_information():
    user_ip = request.cookies.get("user_ip_information")

    return render_template("ip_information.html", user_ip=user_ip)

# Tambien funciona con solo app.run()
if __name__ == '__main__':
    app.run(debug=True) 
    # En entornos de producción el debug=True se va, porque si ocurre un error, revela el back al cliente,
    # y eso es un error de seguridad.