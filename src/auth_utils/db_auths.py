
class SqlServerAuthenticator:

    def __init__(self, username, password, server, database, driver):
        self.username = username
        self.password = password
        self.server = server
        self.database = database
        self.driver = driver
        
    def get_connection_string(self):
        return f"mssql+pyodbc://{self.username}:{self.password}@{self.server}/{self.database}?driver={self.driver}"
