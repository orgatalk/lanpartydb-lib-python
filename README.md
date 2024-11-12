# Python library for the OrgaTalk LAN Party Database

This library provides

- party and party series models,
- functionality to deserialize parties and party series from TOML, and
- functionality to serialize parties (but not party series) to TOML

to work with data for and from the public [LAN party database by
OrgaTalk](https://lanpartydb.orgatalk.de/).

Data and code repositories for the project are available at:
https://github.com/lanpartydb


## Installation

With pip:

```sh
$ pip install lanpartydb
```

Or with [uv](https://docs.astral.sh/uv/):

```sh
$ uv init
$ uv add lanpartydb
```


## Usage

To serialize a party with only the required attributes to TOML:

```py
from datetime import date

from lanpartydb.models import Party
from lanpartydb.writing import serialize_party

party = Party(
    slug='megalan-2023',
    title='MegaLAN 2023',
    start_on=date(2023, 11, 17),
    end_on=date(2023, 11, 19),
)

toml = serialize_party(party)

print(toml)
```

And to serialize a party with all available attributes to a TOML file:

```py
from datetime import date
from decimal import Decimal
from pathlib import Path

from lanpartydb.models import Links, Location, Party, Resource
from lanpartydb.writing import serialize_party

party = Party(
    slug='superlan-2024',
    title='SuperLAN 2024',
    series_slug='superlan',
    organizer_entity='SuperLAN Association',
    start_on=date(2024, 5, 24),
    end_on=date(2024, 5, 26),
    seats=420,
    attendees=397,
    online=False,
    location=Location(
        name='City Hall',
        country_code='us',
        city='Los Angeles',
        zip_code='90099',
        street='123 North Hill Street',
        latitude=Decimal('34.06101057935884'),
        longitude=Decimal('-118.23974355902666'),
    ),
    links=Links(
        website=Resource(
            url='https://www.superlan.example/',
            offline=False,
        ),
    ),
)

toml = serialize_party(party)

path = Path('./superlan-2024.toml')
path.write_text(toml)
```

Take a look at the code (in `src/`) and the tests (in `tests/`) to learn
more about the library's interface.


## License

MIT


## Author

Jochen Kupperschmidt
