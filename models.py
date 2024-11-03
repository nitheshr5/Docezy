from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base  # Ensure this is the correct import for your Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)

class Document(Base):
    __tablename__ = 'documents'
    
    id = Column(Integer, primary_key=True)
    document_metadata = Column(String)  # Keeping this as is
    file_url = Column(String)
    additional_metadata = Column(String)  # Renamed from 'metadata' to 'additional_metadata'
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User")


