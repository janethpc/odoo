from odoo import http
from odoo.http import request

class CustomController(http.Controller):

    @http.route('/reto', auth='user')
    def reto_route(self, **kwargs):
        user = request.env.user
        if user:
            message = f'Hello {user.name}!'
        else:
            message = 'Hello World!'
        
        return """
        <html>
        <head><title>Respuesta Personalizada</title></head>
        <body>
            <h1>Respuesta Personalizada</h1>
            <p>{}</p>
        </body>
        </html>
        """.format(message)
