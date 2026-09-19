# from sqlalchemy import create_engine, Column, Integer, String
# from sqlalchemy.orm import declarative_base, sessionmaker
# import psycopg2

# # 1. Connect to PostgreSQL
# DATABASE_URL = "postgresql+psycopg2://postgres:your_password@localhost:5432/my_db"
# engine = create_engine(DATABASE_URL)

# # 2. Define the Table Structure
# Base = declarative_base()

# class Tshirts(Base):
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key=True)
#     color = Column(String)
#     frequencies = Column(Integer)

# # Create the table if it doesn't exist
# Base.metadata.create_all(engine)
    
# # 3. Open a Session and Save Data
# Session = sessionmaker(bind=engine)
# session = Session()

# # Create a new user object
# new_color = Tshirts(color=tshirt_colors, frequencies=frequency)

# # Add and commit to the database
# session.add(new_color)
# session.commit()

# print("Data saved successfully!")
# session.close()
