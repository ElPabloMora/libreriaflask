import pymysql


def conect_db():
    return pymysql.connect(host='localhost', user='root',passwd='password',db='proyectomicroservicio')