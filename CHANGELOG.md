# Changelog


## 0.9.1 (2024-11-13)

- Added description, usage examples to README.


## 0.9.0 (2024-11-03)

- Fixed parsing of empty series document.

- Changed type of ``Series`` fields ``alternative_names``,
  ``country_codes`` from ``set[str]`` to ``list[str]``.

- Fixed serialization of party location's latitude and longitude.

- Added testing infrastructure (pytest, GitHub Action).

- Added tests for party, series reading.

- Added tests for party serialization.

- Added ruff as a development dependency.

- Updated repository URL.


## 0.8.0 (2024-10-25)

- Raised minimum required tomlkit version to 0.13.2.

- Switched package/project manager from rye to uv.


## 0.7.0 (2024-07-01)

- Added optional ``country_codes`` property to ``Series``.


## 0.6.0 (2024-06-30)

- Added module to write a party to a TOML document.


## 0.5.0 (2024-06-30)

- Removed support to load website URL from ``links.website``. From now
  on, it is expected only in ``links.website.url``.


## 0.4.0 (2024-06-30)

- Generalized name of model ``Website`` to ``Resource``.


## 0.3.0 (2024-05-16)

- Added optional ``attendees`` property to ``Party``.

- Added support for Python 3.12.


## 0.2.0 (2024-02-21)

- Added module to load models from TOML data.


## 0.1.0 (2024-02-21)

- Added models.
