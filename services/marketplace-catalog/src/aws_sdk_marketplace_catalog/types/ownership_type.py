"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#OwnershipType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_marketplace_catalog.errors import DeserializationError

OwnershipType: TypeAlias = Literal[
    "SELF",
    "SHARED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SELF",
        "SHARED",
    )
)


def serialize_json(value: OwnershipType) -> str:
    return value


def deserialize_json(data: str) -> OwnershipType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OwnershipType value: {data!r}")
    return cast(OwnershipType, data)
