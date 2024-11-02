"""
lanpartydb.reading
~~~~~~~~~~~~~~~~~~

Data reading

:Copyright: 2024 Jochen Kupperschmidt
:License: MIT
"""

from decimal import Decimal
from pathlib import Path
import tomllib
from typing import Any

from .models import Links, Location, Party, Resource, Series


# series


def read_series_list_from_toml_file(filename: Path) -> list[Series]:
    """Read list of series from a TOML file."""
    toml = filename.read_text()
    return read_series_list_from_toml(toml)


def read_series_list_from_toml(toml: str) -> list[Series]:
    """Read list of series from a TOML document."""
    data = _load_toml(toml)
    return _read_series_list_from_dict(data)


def _read_series_list_from_dict(data: dict[str, Any]) -> list[Series]:
    """Read list of series from a dictionary."""
    return [Series(**item) for item in data.get('series', [])]


# party


def read_party_from_toml_file(filename: Path) -> Party:
    """Read party from a TOML file."""
    toml = filename.read_text()
    return read_party_from_toml(toml)


def read_party_from_toml(toml: str) -> Party:
    """Read party from a TOML document."""
    data = _load_toml(toml)
    return _read_party_from_dict(data)


def _read_party_from_dict(party_dict: dict[str, Any]) -> Party:
    """Read party from a dictionary."""
    location_dict = party_dict.pop('location', None)
    if location_dict:
        party_dict['location'] = Location(**location_dict)

    links_dict = party_dict.pop('links', None)
    if links_dict:
        website_dict = links_dict.pop('website', None)
        if website_dict:
            website = Resource(
                url=website_dict['url'],
                offline=website_dict.get('offline', False),
            )
            party_dict['links'] = Links(website=website)

    return Party(**party_dict)


# util


def _load_toml(toml: str) -> str:
    return tomllib.loads(toml, parse_float=Decimal)
