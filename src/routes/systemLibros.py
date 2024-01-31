from flask import Blueprint, render_template, flash, redirect, url_for, request
from database.database import conect_db
from models.login_required import login_required

connect=conect_db()
cursor = connect.cursor()

systemlibros = Blueprint('systemlibros',__name__)


@systemlibros.route('/libros', methods=['GET','POST'])
@login_required
def libros():
    cursor.execute('SELECT * FROM itemsbooks')
    libros = cursor.fetchall()
    return render_template('libros.html', data = libros)

@systemlibros.route('/libros/show/<id>', methods=['GET','POST'])
@login_required
def showbook(id):
    cursor.execute('SELECT * FROM itemsbooks WHERE id ={}'.format(id))
    libro = cursor.fetchone()
    return render_template('plantillabook.html', data = libro)

@systemlibros.route('/comprar/libro/<id>')
def comprar(id):
    cursor.execute('SELECT * FROM itemsbooks WHERE id ={}'.format(id))
    data = cursor.fetchone()
    return render_template('carritodecompras.html', libro = data)
