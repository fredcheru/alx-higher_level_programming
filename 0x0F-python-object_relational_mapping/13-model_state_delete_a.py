#!/usr/bin/python3
"""Module that deletes states containing the letter\
        "a" from a MySQL database using SQLAlchemy."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    # Create the SQLAlchemy engine using the provided MySQL credentials
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create a session factory
    Session = sessionmaker(bind=engine)
    # Create a session object
    session = Session()
    # Retrieve all states from the database
    for state in session.query(State):
        # Check if the state's name contains the letter "a"
        if "a" in state.name:
            # Delete the state from the session
            session.delete(state)
    # Commit the session to persist the changes
    session.commit()

0x0F-python-object_relational_mapping/14-model_city_fetch_by_state.py

#!/usr/bin/python3
"""Module that retrieves and prints a list of cities with their\
        associated states from a MySQL database using SQLAlchemy.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City

if __name__ == "__main__":
    # Create the SQLAlchemy engine using the provided MySQL credentials
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    # Create a session factory
    Session = sessionmaker(bind=engine)
    # Create a session object
    session = Session()
    # Retrieve cities and their associated states from the database
    # by joining the City and State tables based on the state_id
    # and ordering the results by city ID
    for city, state in session.query(City, State) \
                              .filter(City.state_id == State.id) \
                              .order_by(City.id):
        # Print the city and state information
        print("{}: ({}) {}".format(state.name, city.id, city.name))
