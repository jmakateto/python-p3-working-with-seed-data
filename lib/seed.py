from faker import Faker
import random
from sqlalchemy.orm import Session
from models import Game, engine

# Create a SQLAlchemy session
session = Session(bind=engine)

fake = Faker()

# Clear existing data
session.query(Game).delete()
session.commit()

# Generate and save random game data
games = [
    Game(
        title=fake.name(),
        genre=fake.word(),
        platform=fake.word(),
        price=random.randint(0, 60)
    )
    for _ in range(50)
]

session.bulk_save_objects(games)
session.commit()

print("Data seeded successfully!")
