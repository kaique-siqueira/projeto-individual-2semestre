import smtplib
import email.message
from lost import senha
from lost import token
from datetime import datetime
from re import S
import psutil
import speedtest
import time 
import mysql.connector
from mysql.connector import errorcode

st = speedtest.Speedtest(secure=1)

st.get_best_server()

while True:

    try:
        db_connection = mysql.connector.connect(
            host='localhost', user='root', password='siqueira300', database='fronttier2')
        print("Conectei no banco!")
    except mysql.connector.Error as error:
        if error.errno == errorcode.ER_BAD_DB_ERROR:
             print("Não encontrei o banco")
        elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
           print("Credenciais erradas")
        else:
           print(error) 
           

    #rede
    ping = st.results.ping
    download = round(st.download() / 1000 / 1000, 1)
    upload = round(st.upload() / 1000 / 1000, 1)
    
    #ping2 = st.results.ping * 2
    #download2 = round(st.download() / 1000 / 1000 * 0.5, 1)
    #pload2 = round(st.upload() / 1000 / 1000 * 1.5, 1)

    #ping3 = st.results.ping * 3
    #download3 = round(st.download() / 1000 / 1000 * 1.5, 1)
    #upload3 = round(st.upload() / 1000 / 1000 * 0.5, 1)        
    

    # psutil.cpu_percent()
    discoTotal = round(psutil.disk_usage('/').total*(2**-30),2)
    memoriaTotal = round(psutil.virtual_memory().total*(2**-30),2)           
    
    # CPU
    freqAtual = psutil.cpu_freq().current
    percentualCpu = psutil.cpu_percent()

    # freqMin = psutil.cpu_freq().min
    # freqMax = psutil.cpu_freq().max

# DISK
    discoUsado = round(psutil.disk_usage('/').used*(2**-30),2)
    percentualDisco = round(discoUsado / discoTotal,3)

    # discoLivre = round(discoTotal - discoUsado,2)

# MEMORY
    memoriaUsada = round(psutil.virtual_memory().used*(2**-30),2)
    percentualMemoria = round(memoriaUsada / memoriaTotal,3)

    # memoriaLivre = round(memoriaUsada / memoriaTotal,2)

# SIMULATION
    percentualCpu2 = percentualCpu + 10 if (percentualCpu <= 90) else 100.0
    percentualCpu3 = percentualCpu2 + 5 if (percentualCpu2 <= 95) else 100.0

    percentualDisco2 = percentualDisco - 0.05 if (percentualDisco >= 0.05) else 0.0
    percentualDisco3 = percentualDisco2 * 3 if ((percentualDisco2 * 3) <= 1) else 1

    percentualMemoria2 = percentualMemoria + 0.15 if (percentualMemoria <= 0.85) else 1
    percentualMemoria3 = percentualMemoria2 - 0.05

    discoUsado2 = round(discoTotal * percentualDisco2,2)
    # discoLivre2 = discoTotal - discoUsado2
    discoUsado3 = round(discoTotal * percentualDisco3,2)
    # discoLivre3 = discoTotal - discoUsado3

    memoriaUsada2 = round(memoriaTotal * percentualMemoria2,2)
    # memoriaLivre2 = memoriaTotal - memoriaUsada2
    memoriaUsada3 = round(memoriaTotal * percentualMemoria3,2)
    # memoriaLivre3 = memoriaTotal - memoriaUsada3

    dataHora = datetime.now()
    formatoh = dataHora.strftime("%d/%m/%Y %H:%M:%S")

    
    cursor = db_connection.cursor()
    
    # select = "select * from maquinaServidor where idServidor;"
    # cursor.execute(select)

    fkServidor = 3
    sql = "INSERT INTO Dados(dataHora, freqAtual, percentualCpu, discoUsado, memoriaUsada, download, upload, ping) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    values = [dataHora, freqAtual, percentualCpu, discoUsado, memoriaUsada, download, upload, ping]
    cursor.execute(sql, values)

    # sql = "INSERT INTO dados(dataHora, freqAtual, percentualCpu, discoUsado, memoriaUsada) VALUES (%s,%s,%s,%s,%s)"
    # values = [dataHora, freqAtual, percentualCpu2, discoUsado2, memoriaUsada2]
    # cursor.execute(sql, values)

    # sql = "INSERT INTO dados(dataHora, freqAtual, percentualCpu, discoUsado, memoriaUsada) VALUES (%s,%s,%s,%s,%s)"
    # values = [dataHora, freqAtual, percentualCpu3, discoUsado3, memoriaUsada3]
    # cursor.execute(sql, values)

    
    print("\n")
    print(cursor.rowcount, "Inserindo no banco.")

    db_connection.commit()
    db_connection.close()    
    time.sleep(0.1)
