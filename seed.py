# seed.py

from models import Base, engine, session, Dev, Company, Freebie
from sqlalchemy import delete

# Optional: Clear existing data (useful for reseeding)
session.execute(delete(Freebie))
session.execute(delete(Dev))
session.execute(delete(Company))
session.commit()

# Create tables
Base.metadata.create_all(engine)

# Create Companies
google = Company(name="Google", founding_year=1998)
microsoft = Company(name="Microsoft", founding_year=1975)

# Create Devs
flavian = Dev(name="Flavian Mecha")
virginia = Dev(name="Virginia Wanjiru")

# Give Freebies
google.give_freebie(flavian, "T-shirt", 100)
microsoft.give_freebie(virginia, "Mug", 50)

# Save all to DB
session.add_all([google, microsoft, flavian, virginia])
session.commit()

print("✅ Database seeded successfully!")
