import speedtest
import time
import mysql.connector
from mysql.connector import Error
from datetime import datetime

st = speedtest.Speedtest()

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


    ping = st.results.ping
    download = round(st.download() / 1000 / 1000, 1)
    upload = round(st.upload() / 1000 / 1000, 1)


    dataHora = datetime.now()
    formatoh = dataHora.strftime("%d/%m/%Y %H:%M:%S")


    cursor = db_connection.cursor()
    sql = "INSERT INTO internet (dataHora, download, upload, ping) VALUES (%s,%s,%s, %s)"
    values = [dataHora, download, upload, ping]
    cursor.execute(sql, values)

   # print(f"Your ping is: {st.results.ping} ms")
   # print(f"Your download speed: {round(st.download() / 1000 / 1000, 1)} Mbit/s")
   # print(f"Your upload speed: {round(st.upload() / 1000 / 1000, 1)} Mbit/s")


    print("\n")
    print(cursor.rowcount, "Inserindo no banco.")

    db_connection.commit()
    db_connection.close()  

    time.sleep(1.0)


