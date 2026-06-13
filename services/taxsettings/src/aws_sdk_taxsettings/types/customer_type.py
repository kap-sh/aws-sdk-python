"""Generated from Smithy shape ``com.amazonaws.taxsettings#CustomerType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_taxsettings.errors import DeserializationError

CustomerType: TypeAlias = Literal[
    "Business",
    "Individual",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Business",
        "Individual",
    )
)


def serialize_json(value: CustomerType) -> str:
    return value


def deserialize_json(data: str) -> CustomerType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CustomerType value: {data!r}")
    return cast(CustomerType, data)
