"""
:Copyright: 2024 Jochen Kupperschmidt
:License: MIT
"""

import pytest

from lanpartydb.models import Series
from lanpartydb.reading import read_series_list_from_toml


@pytest.mark.parametrize(
    ('toml', 'expected'),
    [
        (
            """
            """,
            [],
        ),
        (
            """
            [[series]]
            slug = "megalan"
            name = "MegaLAN"
            """,
            [
                Series(
                    slug='megalan',
                    name='MegaLAN',
                    alternative_names=[],
                    country_codes=[],
                ),
            ],
        ),
        (
            """
            [[series]]
            slug = "gammalan"
            name = "GammaLAN"
            country_codes = ["ca", "us"]

            [[series]]
            slug = "deltalan"
            name = "DeltaLAN"
            alternative_names = ["Δ LAN", "Δέλτα LAN"]
            country_codes = ["au"]
            """,
            [
                Series(
                    slug='gammalan',
                    name='GammaLAN',
                    alternative_names=[],
                    country_codes=['ca', 'us'],
                ),
                Series(
                    slug='deltalan',
                    name='DeltaLAN',
                    alternative_names=['Δ LAN', 'Δέλτα LAN'],
                    country_codes=['au'],
                ),
            ],
        ),
    ],
)
def test_read_series_list_from_toml(toml: str, expected: list[Series]):
    assert read_series_list_from_toml(toml) == expected
