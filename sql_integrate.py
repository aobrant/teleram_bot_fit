import os
from sqlalchemy import create_engine

username = os.getenv.get('DB_USERNAME')
password = os.getenv.get('DB_PASSWORD')
host = os.getenv.get('DB_HOST')
dbname = os.getenv.get('DB_NAME')
eengine = create_engine(f'postgresql://{username}:{password}@{host}/{dbname}')
