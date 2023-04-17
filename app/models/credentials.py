from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.init_db import Base

class Credentials(Base):
    __tablename__ = "credentials"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    username = Column(String, index=True)
    email = Column(String, index=True)
    hashed_password = Column(String)

    user = relationship("User", back_populates="credentials")