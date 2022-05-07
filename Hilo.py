import os
from datetime import datetime
import shutil
from time import sleep, time
import logging
import main
import mail

logging.basicConfig(
    filename=os.path.join('c:\\Pedidos\\Logs',datetime.now().strftime("%d-%m-%Y")+".txt" ), filemode='w',
    format='%(asctime)s | %(levelname)s: %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p',level=logging.DEBUG)
    
entrada = "c:\\Pedidos\\Entrada"
temp = "c:\\Pedidos\\Temp"
salida = "c:\\Pedidos\\Salida"

while(True):
    if(len(os.listdir(entrada)) > 0):
        for file in os.listdir(entrada):
            if os.path.isfile(os.path.join(entrada,file)) :
                if file.find(".pdf") > 0  or file.find(".PDF"):
                    logging.info("Archivo valido en contrado: "+ file)
                    main.generaExcel(os.path.join(entrada,file),salida)
                else:
                    logging.info("Archivo no valido en contrado: "+ file+" Eliminado")
                    os.remove(os.path.join(entrada,file))
                    mail.senMail("Archivo no valido en contrado: "+ file+" Eliminado")
            else: 
                if os.path.isdir(os.path.join(entrada,file)):
                    logging.info("Se en contro un directorio no valido, eliminado")
                    shutil.rmtree(os.path.join(entrada,file))
                    mail.senMail("Se en contro un directorio no valido, eliminado")
                else:
                    logging.info("Elemento encotrado no valido, eliminado")
                    os.remove(os.path.join(entrada,file))
                    mail.senMail("Elemento encotrado no valido, eliminado")
    else:
        logging.info("No se en contraron archivos para procesar" )
        sleep(60)