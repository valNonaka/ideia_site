import mysql.connector
from mysql.connector import errorcode

try:
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password=''  # Replace with your actual password
    )
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Existe algo errado no nome de usuário ou senha')
    else:
        print(err)

# Check if connection is successful before creating a cursor

if conn.is_connected():
    cursor = conn.cursor()

    # Create database
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS resources;")
        print("Database 'resources' created successfully.")
    except mysql.connector.Error as err:
        print(f"Error creating database: {err}")

    # Use the 'resources' database
    try:
        cursor.execute("USE resources;")
        print("Using 'resources' database.")
    except mysql.connector.Error as err:
        print(f"Error selecting database: {err}")

# Create tables
TABLES = {
    'science': '''
        CREATE TABLE `science` (
        id int(11) NOT NULL AUTO_INCREMENT,
        title varchar(50) NOT NULL,
        description varchar(40) NOT NULL,
        link varchar(300) NOT NULL,
        PRIMARY KEY (`id`)
        )
    ''',
    'math': '''
        CREATE TABLE `math` (
        id int(11) NOT NULL AUTO_INCREMENT,
        title varchar(50) NOT NULL,
        description varchar(40) NOT NULL,
        link varchar(300) NOT NULL,
        PRIMARY KEY (`id`)
        ) 
    ''',
    'statistic': '''
        CREATE TABLE `statistic` (
        id int(11) NOT NULL AUTO_INCREMENT,
        title varchar(50) NOT NULL,
        description varchar(50) NOT NULL,
        link varchar(300) NOT NULL,
        PRIMARY KEY (`id`)
        ) 
    ''',
    'econometrics': '''
        CREATE TABLE `econometrics` (
        id int(11) NOT NULL AUTO_INCREMENT,
        title varchar(50) NOT NULL,
        description varchar(50) NOT NULL,
        link varchar(300) NOT NULL,
        PRIMARY KEY (`id`)
        ) 
    ''',
    'coding': '''
        CREATE TABLE `coding` (
        id int(11) NOT NULL AUTO_INCREMENT,
        title varchar(50) NOT NULL,
        description varchar(50) NOT NULL,
        link varchar(300) NOT NULL,
        PRIMARY KEY (`id`)
        ) 
    ''',
      'eda': '''
        CREATE TABLE `coding` (
        id int(11) NOT NULL AUTO_INCREMENT,
        title varchar(50) NOT NULL,
        description varchar(50) NOT NULL,
        link varchar(300) NOT NULL,
        PRIMARY KEY (`id`)
        ) 
    ''',
    'ml': '''
        CREATE TABLE `ml` (
        id int(11) NOT NULL AUTO_INCREMENT,
        title varchar(50) NOT NULL,
        description varchar(50) NOT NULL,
        link varchar(300) NOT NULL,
        PRIMARY KEY (`id`)
        ) 
    ''',
    'dl': '''
        CREATE TABLE `dl` (
        id int(11) NOT NULL AUTO_INCREMENT,
        title varchar(50) NOT NULL,
        description varchar(50) NOT NULL,
        link varchar(300) NOT NULL,
        PRIMARY KEY (`id`)
        ) 
    ''',
    'mlop': '''
        CREATE TABLE `mlop` (
        id int(11) NOT NULL AUTO_INCREMENT,
        title varchar(50) NOT NULL,
        description varchar(50) NOT NULL,
        link varchar(300) NOT NULL,
        PRIMARY KEY (`id`)
        ) 
    '''
}


for tabela_nome in TABLES:
    tabela_sql = TABLES[tabela_nome]
    try:
        print('Criando tabela {}:'.format(tabela_nome), end=' ')
        cursor.execute(tabela_sql)
        print('OK')
    except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print('Já existe')
            else:
                print(err.msg)

    # Close the cursor and connection
cursor.close()
conn.close()
