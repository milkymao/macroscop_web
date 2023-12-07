import macroscop_web as mc
import mysqlconn_settings as db_conn

db = db_conn.DataBase(password='admin123')
db.insert_data(values=mc.Macroscop(host='localhost:8080').get_data())