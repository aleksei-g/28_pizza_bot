from database import init_db, db_session
from models import Pizza, PizzaChoices, catalog


init_db()

for pizza in catalog:
    new_item = Pizza(title=pizza.get('title'),
                     description=pizza.get('description'))
    for pizza_choice in pizza.get('choices'):
        new_item.choices.append(PizzaChoices(title=pizza_choice.get('title'),
                                             price=pizza_choice.get('price')))
    db_session.add(new_item)
db_session.commit()
