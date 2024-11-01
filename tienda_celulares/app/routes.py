from flask import render_template, request, redirect, url_for, Blueprint
from .models import db, Producto, Categoria, Modelo, Equipo

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/gestionar_productos', methods=['GET', 'POST'])
def gestionar_productos():
    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = float(request.form['precio'])
        cantidad = int(request.form['cantidad'])
        categoria_id = int(request.form['categoria_id'])
        modelo_id = int(request.form['modelo_id'])

        nuevo_producto = Producto(nombre=nombre, precio=precio, cantidad=cantidad, categoria_id=categoria_id, modelo_id=modelo_id)
        db.session.add(nuevo_producto)
        db.session.commit()
        return redirect(url_for('main.gestionar_productos'))

    categorias = Categoria.query.all()
    modelos = Modelo.query.all()
    productos = Producto.query.all()
    return render_template('gestionar_productos.html', productos=productos, categorias=categorias, modelos=modelos)

@main_bp.route('/gestionar_categorias', methods=['GET', 'POST'], endpoint="gestionar_categorias")
def gestionar_categorias():
    if request.method == 'POST':
        nombre = request.form['nombre']
        nueva_categoria = Categoria(nombre=nombre)
        db.session.add(nueva_categoria)
        db.session.commit()
        return redirect(url_for('main.gestionar_categorias'))

    categorias = Categoria.query.all()
    return render_template('gestionar_categorias.html', categorias=categorias)

@main_bp.route('/vender', methods=['GET', 'POST'])
def vender():
    if request.method == 'POST':
        # Lógica para registrar la venta
        pass
    productos = Producto.query.all()
    return render_template('vender.html', productos=productos)
@main_bp.route('/equipos', methods=['GET'])
def equipos():
    equipos = Equipo.query.all()  # Asegúrate de que 'Equipo' es el nombre de tu modelo
    return render_template('equipos.html', equipos=equipos)

# En routes.py
@main_bp.route('/modelos', methods=['GET'], endpoint='modelos')
def modelos():
    modelos = Modelo.query.all()
    return render_template('modelos.html', modelos=modelos)

# @main_bp.route('/categorias', methods=['GET'])
# def gestionar_categorias():
#     categorias = Categoria.query.all()
#     return render_template('categorias.html', categorias=categorias)

@main_bp.route('/equipos/create', methods=['GET', 'POST'])
def create_equipo():
    # Lógica para crear un nuevo equipo
    return render_template('create_equipo.html')



