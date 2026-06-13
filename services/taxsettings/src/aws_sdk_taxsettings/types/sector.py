"""Generated from Smithy shape ``com.amazonaws.taxsettings#Sector``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_taxsettings.errors import DeserializationError

Sector: TypeAlias = Literal[
    "Business",
    "Individual",
    "Government",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Business",
        "Individual",
        "Government",
    )
)


def serialize_json(value: Sector) -> str:
    return value


def deserialize_json(data: str) -> Sector:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Sector value: {data!r}")
    return cast(Sector, data)
