from sqlalchemy import create_engine
from src.auth_utils.db_auths import SqlServerAuthenticator
import pandas as pd

class SpotifyLoader:

    def __init__(self, username, password, server, database, driver):

        connection_string = SqlServerAuthenticator(username, password, server, database, driver).get_connection_string()
        self.engine = create_engine(connection_string)

    def load_to_sql(self, dataframe: pd.DataFrame, table_name: str, if_exists='append'):

        try:
            if dataframe.empty:
                print("Empty Dataframe")
                return

            dataframe.to_sql(name=table_name, con=self.engine, if_exists=if_exists, index=False)
            print(f"Success")
        except Exception as e:
            print(f"Error: {str(e)}")
