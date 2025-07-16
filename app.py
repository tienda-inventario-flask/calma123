# GeniusKeys_SalesPage_Web/app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Renderiza tu archivo HTML de página de ventas
    return render_template('sales_page_simple.html')

if __name__ == '__main__':
    # Puedes cambiar el puerto si lo necesitas, por defecto 5000
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))