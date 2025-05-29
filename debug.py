# debug.py

from models import session, Dev, Company, Freebie

# Fetch all records to explore easily
devs = session.query(Dev).all()
companies = session.query(Company).all()
freebies = session.query(Freebie).all()

# Try a few useful queries
first_dev = session.query(Dev).first()
first_company = session.query(Company).first()
first_freebie = session.query(Freebie).first()



