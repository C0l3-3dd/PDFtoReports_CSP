#from cgitb import text
from reportlab.pdfgen import canvas



def create(datos,name): 
    c = canvas.Canvas(name,pagesize=( 311.85 ,85.0394))
    h = 85.0394#3.00 cm alto   -> y
    w = 311.85#11.00 cm largo  -> x 
    nombres = ['Maru','Male','Martha','Yola']
    k = 0
    for objeto in datos:

        nveces= round( len(objeto)  / 3)
        sobrante = len(objeto) % 3
        if sobrante == 2:
            nveces = nveces - 1

        i=0
        for data in range( nveces):
            
            valortienda = str(objeto[i].get('tienda'))
            valorproducto = objeto[i].get('produtos')
            valorproductoP = objeto[i].get('nameProducto')
            #---------Izquierda
            codigoModelo = c.beginText(2,h-15)
            tienda = c.beginText(2, (h/2)-3)
            producto = c.beginText(2,h-(h-10))

            codigoModelo.setFont("Courier-Bold",12)
            tienda.setFont("Helvetica",25)
            producto.setFont("Helvetica",28)

            codigoModelo.textLine(valorproductoP)
            tienda.textLine('T - ' + str(valortienda))
            producto.textLine('P - '+ str(valorproducto))

            c.drawText(codigoModelo)
            c.drawText(tienda)
            c.drawText(producto)
            #---------Izquierda
            #---------Centro
            valortienda = str(objeto[i+1].get('tienda'))
            valorproducto = objeto[i+1].get('produtos')
            valorproductoP = objeto[i+1].get('nameProducto')
            codigoModelo = c.beginText(110,h-15)
            tienda = c.beginText(110, (h/2)-3)
            producto = c.beginText(110,h-(h-10))

            codigoModelo.setFont("Courier-Bold",12)
            tienda.setFont("Helvetica",25)
            producto.setFont("Helvetica",28)

            codigoModelo.textLine(valorproductoP)
            tienda.textLine('T - ' + str(valortienda))
            producto.textLine('P - '+ str(valorproducto))

            c.drawText(codigoModelo)
            c.drawText(tienda)
            c.drawText(producto)
            #---------Centro
            #---------Derecha
            valortienda = str(objeto[i+2].get('tienda'))
            valorproducto = objeto[i+2].get('produtos')
            valorproductoP = objeto[i+2].get('nameProducto')
            codigoModelo = c.beginText(210,h-15)
            tienda = c.beginText(210, (h/2)-3)
            producto = c.beginText(210,h-(h-10))

            codigoModelo.setFont("Courier-Bold",12)
            tienda.setFont("Helvetica",25)
            producto.setFont("Helvetica",28)

            codigoModelo.textLine(valorproductoP)
            tienda.textLine('T - ' + str(valortienda))
            producto.textLine('P - '+ str(valorproducto))

            c.drawText(codigoModelo)
            c.drawText(tienda)
            c.drawText(producto)
            #---------Derecha
            c.showPage()
            i += 3

        if sobrante == 1:
            valortienda = str(objeto[-1].get('tienda'))
            valorproducto = objeto[-1].get('produtos')
            valorproductoP = objeto[-1].get('nameProducto')
            #---------Izquierda
            codigoModelo = c.beginText(2,h-15)
            tienda = c.beginText(2, (h/2)-3)
            producto = c.beginText(2,h-(h-10))

            codigoModelo.setFont("Courier-Bold",12)
            tienda.setFont("Helvetica",25)
            producto.setFont("Helvetica",28)

            codigoModelo.textLine(valorproductoP)
            tienda.textLine('T - ' + str(valortienda))
            producto.textLine('P - '+ str(valorproducto))

            c.drawText(codigoModelo)
            c.drawText(tienda)
            c.drawText(producto)
            #---------Izquierda
            c.showPage()

        if sobrante == 2:
            valortienda = str(objeto[-1].get('tienda'))
            valorproducto = objeto[-1].get('produtos')
            valorproductoP = objeto[-1].get('nameProducto')
            #---------Izquierda
            codigoModelo = c.beginText(2,h-15)
            tienda = c.beginText(2, (h/2)-3)
            producto = c.beginText(2,h-(h-10))

            codigoModelo.setFont("Courier-Bold",12)
            tienda.setFont("Helvetica",25)
            producto.setFont("Helvetica",28)

            codigoModelo.textLine(valorproductoP)
            tienda.textLine('T - ' + str(valortienda))
            producto.textLine('P - '+ str(valorproducto))

            c.drawText(codigoModelo)
            c.drawText(tienda)
            c.drawText(producto)
            #---------Izquierda
            #---------Centro
            valortienda = str(objeto[-2].get('tienda'))
            valorproducto = objeto[-2].get('produtos')
            valorproductoP = objeto[-2].get('nameProducto')
            codigoModelo = c.beginText(110,h-15)
            tienda = c.beginText(110, (h/2)-3)
            producto = c.beginText(110,h-(h-10))

            codigoModelo.setFont("Courier-Bold",12)
            tienda.setFont("Helvetica",28)
            producto.setFont("Helvetica",28)

            codigoModelo.textLine(valorproductoP)
            tienda.textLine('T - ' + str(valortienda))
            producto.textLine('P - '+ str(valorproducto))

            c.drawText(codigoModelo)
            c.drawText(tienda)
            c.drawText(producto)
            #---------Centro
            c.showPage()

        #c.showPage()
        #---------separador
        #----Izquirdo
        codigoModelo = c.beginText(30,h-15)
        tienda = c.beginText(20, (h/2)+5)
        producto = c.beginText(30,h-(h-10))

        codigoModelo.setFont("Courier-Bold",15)
        tienda.setFont("Helvetica",15)
        producto.setFont("Helvetica",15)

        codigoModelo.textLine('▲')
        tienda.textLines('Fin\nInicio')
        producto.textLine('▼')

        c.drawText(codigoModelo)
        c.drawText(tienda)
        c.drawText(producto)
        #----Izquirdo
        #----Centro
        codigoModelo = c.beginText(130,h-15)
        tienda = c.beginText(120, (h/2)+5)
        producto = c.beginText(130,h-(h-10))

        codigoModelo.setFont("Courier-Bold",15)
        tienda.setFont("Helvetica",15)
        producto.setFont("Helvetica",15)

        codigoModelo.textLine('▲')
        nfin =''
        ninicio=''
        if(k < 3):
            nfin = nombres[k]
            ninicio = nombres[k+1]
        else:
            nfin = nombres[k]

        tienda.textLines(nfin+'\n'+ninicio)
        producto.textLine('▼')

        c.drawText(codigoModelo)
        c.drawText(tienda)
        c.drawText(producto)
        #----Centro
        #----Derecho
        codigoModelo = c.beginText(235,h-15)
        tienda = c.beginText(220, (h/2)+5)
        producto = c.beginText(230,h-(h-10))

        codigoModelo.setFont("Courier-Bold",15)
        tienda.setFont("Helvetica",15)
        producto.setFont("Helvetica",15)

        codigoModelo.textLine('▲')
        tienda.textLines('Fin\nInicio')
        producto.textLine('▼')

        c.drawText(codigoModelo)
        c.drawText(tienda)
        c.drawText(producto)
        #----Derecho
        #---------separador
        c.showPage()
        k=k+1

    c.showPage()
    c.save()