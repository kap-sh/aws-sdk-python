"""Generated from Smithy shape ``com.amazonaws.taxsettings#PersonType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_taxsettings.errors import DeserializationError

PersonType: TypeAlias = Literal[
    "Legal Person",
    "Physical Person",
    "Business",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Legal Person",
        "Physical Person",
        "Business",
    )
)


def serialize_json(value: PersonType) -> str:
    return value


def deserialize_json(data: str) -> PersonType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PersonType value: {data!r}")
    return cast(PersonType, data)
