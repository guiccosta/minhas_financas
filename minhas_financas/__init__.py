# type: ignore[attr-defined]
"""Projeto que desenvolverei para acompanhar minha carteira de investimentos, renda fixa, gastos, e etc, utilizando ferramentas em python, google sheets e Looker Studio."""

import sys

if sys.version_info >= (3, 8):
    from importlib import metadata as importlib_metadata
else:
    import importlib_metadata


def get_version() -> str:
    try:
        return importlib_metadata.version(__name__)
    except importlib_metadata.PackageNotFoundError:  # pragma: no cover
        return "unknown"


version: str = get_version()
