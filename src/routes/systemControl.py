from flask import Blueprint,render_template, flash, redirect, url_for, request

systemcontrol = Blueprint('systemcontrol',__name__)


@systemcontrol.route('/mainprimary', methods=['GET','POST'])
def mainprimary():
    return render_template('mainprimary.html')

