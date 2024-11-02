"""
:Copyright: 2024 Jochen Kupperschmidt
:License: MIT
"""

from datetime import date
from decimal import Decimal
from textwrap import dedent

import pytest

from lanpartydb.models import Links, Location, Party, Resource
from lanpartydb.writing import serialize_party


@pytest.mark.parametrize(
    ('party', 'expected'),
    [
        (
            Party(
                slug='megalan-2023',
                title='MegaLAN 2023',
                start_on=date(2023, 11, 17),
                end_on=date(2023, 11, 19),
            ),
            dedent("""\
            slug = "megalan-2023"
            title = "MegaLAN 2023"
            start_on = 2023-11-17
            end_on = 2023-11-19
            """),
        ),
        (
            Party(
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
            ),
            dedent("""\
            slug = "superlan-2024"
            title = "SuperLAN 2024"
            series_slug = "superlan"
            organizer_entity = "SuperLAN Association"
            start_on = 2024-05-24
            end_on = 2024-05-26
            seats = 420
            attendees = 397

            [location]
            name = "City Hall"
            country_code = "us"
            city = "Los Angeles"
            zip_code = "90099"
            street = "123 North Hill Street"
            latitude = 34.06101057935884
            longitude = -118.23974355902666

            [links.website]
            url = "https://www.superlan.example/"
            """),
        ),
    ],
)
def test_serialize_party(party: Party, expected: str):
    assert serialize_party(party) == expected
