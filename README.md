Generic single-database configuration

# 🛍️ Freebie Tracker (Phase 3 Code Challenge)

This is a SQLAlchemy-based app that helps developers track all the free swag (freebies) they collect from various companies at hackathons and tech events.

## 🔍 Learning Goals

- Use SQLAlchemy to model relationships between tables
- Perform CRUD operations on a database
- Use ForeignKey, relationship(), and backref() to manage associations
- Write and run migrations with Alembic

## 🧱 Models

### `Dev`
- `name: str`
- Relationships: has many `Freebies`

### `Company`
- `name: str`
- `founding_year: int`
- Relationships: has many `Freebies`, has many `Devs` through `Freebies`

### `Freebie`
- `item_name: str`
- `value: int`
- `dev_id: FK`
- `company_id: FK`

## 🔄 Setup Instructions

1. Clone this repo
2. Run:

```bash
pipenv install
pipenv shell
alembic upgrade head
python seed.py

