import psycopg2
try:
    connection = psycopg2.connect(user = "sysadmin",
                                  password = "pynative@#29",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "postgres_db")
    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print ( connection.get_dsn_parameters(),"\n")
