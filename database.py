import pymysql
import re

class Database:
    def __init__(self):
        self.connection = pymysql.connect(host='localhost', user='root', password= '', db='empresas_csp')

        self.cursor = self.connection.cursor()
    
    def getProdcuto(self, id):
        sql = 'SELECT codigo, modelo FROM calcetines WHERE id_barras = {}'.format(str(id))
        
        try:
            self.cursor.execute(sql)
            producto = self.cursor.fetchone()
            self.cursor.close()
            
            return producto
        except Exception as e:
            print(e)
            print("prodcuto no econtrado",id)
            producto =[]
            return producto
            
    def getAll(self):
        sql ='SELECT id_barras FROM calcetines'
        regex = re.compile('[0-9]')   
        productos =[]
        try:
            self.cursor.execute(sql)
            for id_barras in self.cursor.fetchall():
                productos.append (str(id_barras).strip("('',)") )
                
            self.cursor.close()

            return productos
        except Exception as e:
            print(e)
            print("Error al obtener datos")
            return productos

    def setFolios(self,folio):
        sql = "INSERT INTO `folios`(`folio`, `estado`) VALUES (%s,'1');"
        try:
            self.cursor.execute(sql, str(folio) )
            self.cursor.connection.commit()
        except Exception as e:
            print(e)

    def setAnularFolios(self,folio):
        sql = "UPDATE folios SET estado = 0 WHERE folio =  %s;"
        try:
            self.cursor.execute(sql, str(folio) )
            self.cursor.connection.commit()
        except Exception as e:
            print(e)

    def getUltimoFolio(self):
        sql ="SELECT id FROM folios WHERE estado = 0 ORDER BY id DESC LIMIT 1;"

        try:
            self.cursor.execute(sql)
            #datos = [datos[0] for datos in self.cursor.fetchall()]
            ultimoFolio = self.cursor.fetchone()
            #print("El utimo id es ---> ",str(ultimoFolio).strip('(,)'))
            return(int(str(ultimoFolio).strip('(,)')))
            
        except Exception as e:
            print(e)
            return(None)

    def getFolios(self,a,b):
        sql = "SELECT folio FROM folios WHERE estado = 1 AND id BETWEEN %s AND %s ORDER BY id ASC;"

        try:
            self.cursor.execute(sql,(a,b))
            data = [data[0] for data in self.cursor.fetchall()]
            #print(data)
            return data
        except Exception as e:
            print(e)
            data = []
            return data 
    
    def getXname(self,codigo,modelo):
        if modelo == '':
            sql = "SELECT * FROM calcetines WHERE codigo = %s;"
        else:
            sql = "SELECT * FROM calcetines WHERE codigo = %s AND modelo = %s;"
        try:
            if modelo == '':
                self.cursor.execute(sql,(codigo))
            else:
                self.cursor.execute(sql,(codigo,modelo))
            data = self.cursor.fetchone()
            return(data[4])
        except Exception as e:
            print(str(e))

database = Database()
#print(database.getAll())

#for i in range(1,2000):
#database.setFolios(2000)
#inicio = database.getUltimoFolio()
#fin = str( int( inicio) + 25 )
#print( database.getFolios(database.getUltimoFolio(), int( inicio) + 25 ) )

#database.getXname('L2','CAFE')