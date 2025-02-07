from sqlalchemy import Column, Integer, String, Boolean
from database.db_connection import Base

class Challenge(Base):
    __tablename__ = "challenges"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False, unique=True)
    author = Column(String(255), nullable=False)
    difficulty = Column(String(50), nullable=False)
    event = Column(String(255), nullable=True)
    category = Column(String(255), nullable=False)
    solved_by_user = Column(Boolean, default=False)
    video_published = Column(Boolean, default=False)
    post_published_medium = Column(Boolean, default=False)

# ✅ Create Table if Not Exists
def create_tables(engine):
    Base.metadata.create_all(engine)
