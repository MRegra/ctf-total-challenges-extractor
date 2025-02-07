import sys
import mariadb
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database Config
DB_USER = "myuser"
DB_PASSWORD = "mypassword"
DB_HOST = "localhost"
DB_PORT = 3306
DB_NAME = "ctf"

# ✅ MariaDB Raw Connection
def get_mariadb_cursor():
    try:
        conn = mariadb.connect(
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME
        )
        print("✅ Connected to MariaDB.")
        return conn.cursor(), conn
    except mariadb.Error as e:
        print(f"❌ Error connecting to MariaDB: {e}")
        sys.exit(1)

# ✅ SQLAlchemy Connection
DATABASE_URL = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?charset=utf8mb4&collation=utf8mb4_unicode_ci"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
