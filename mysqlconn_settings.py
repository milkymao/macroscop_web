import pymysql

class DataBase:
    def __init__(self, host='127.0.0.1', port=3306, user='root', password='', database='test_db2',
                 table='test_table', cursorclass=pymysql.cursors.DictCursor):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.table = table
        self.cursorclass = cursorclass

    # Подключение к БД
    def connection(self):
        return pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password,
                               database=self.database, cursorclass=self.cursorclass)
    # Нерабочий метод!!!
    # def create_db(self):
    #     try:
    #         conn = DataBase.connection(self)
    #         with conn.cursor() as cursor:
    #             query = f"CREATE SCHEMA `{self.database}`;"
    #             cursor.execute(query)
    #         conn.close()
    #     except Exception as ex:
    #         print("Connection refused...")
    #         print(ex)

    # Создание новой таблицы в существующей БД
    def create_table(self):
        try:
            conn = DataBase.connection(self)
            with conn.cursor() as cursor:
                query = (f"CREATE TABLE `{self.database}`.`{self.table}` (`id` VARCHAR(45) NOT NULL,`ext_sys_id` VARCHAR(45) NULL,"
                         f"`ext_id` VARCHAR(45) NULL,`first_name` VARCHAR(45) NULL,`patronymic` VARCHAR(45) NULL,`second_name` VARCHAR(45) NULL,"
                         f"`add_info` TEXT NULL,`mod_time` VARCHAR(45) NULL,`create_time` VARCHAR(45) NULL,`force` TINYINT(1) NULL,"
                         f"`face_images` TEXT NOT NULL,PRIMARY KEY (`id`));")
                cursor.execute(query)
            conn.close()
        except Exception as ex:
            print("Connection refused...")
            print(ex)

    # Занесение данных в БД
    def insert_data(self, values=''):
        try:
            conn = DataBase.connection(self)
            with conn.cursor() as cursor:
                for value in values:
                    if not DataBase.repeat_check(self, value[0]):
                        query = f'INSERT INTO {self.table} VALUES({list_to_str(value)});'
                        cursor.execute(query)
                    conn.commit()
            conn.close()
        except Exception as ex:
            print("Connection refused...")
            print(ex)

    # Проверка на наличие записи в БД
    def repeat_check(self, value=''):
        try:
            conn = DataBase.connection(self)
            with conn.cursor() as cursor:
                    cursor.execute(f"SELECT count(*) FROM {self.table} WHERE id = '{value}';")
                    records = cursor.fetchone()
                    if records['count(*)'] == 0:
                        return False
                    else:
                        return True
                    conn.commit()
        except Exception as ex:
            print("Connection refused...")
            print(ex)

# Перевод в строковый тип данных (Для query)
def list_to_str(list, str=""):
    for el in list:
        if (el == False) or (el == True):
            str += f"{(int((el == 'True') or (el == 'False'))).__str__()}, "
        elif el != list[-1]:
            str += f"'{el}', "
        else:
            str += f"'{el}'"
    return str