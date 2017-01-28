from database import init_db, db_session
from models import Catalog, Choices, catalog


init_db()

for pizza in catalog:
    new_item = Catalog(title=pizza.get('title'),
                       description=pizza.get('description'))
    for choice in pizza.get('choices'):
        new_item.choices.append(Choices(title=choice.get('title'),
                                        price=choice.get('price')))
    db_session.add(new_item)
db_session.commit()
