"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#OfferStateString``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_marketplace_catalog.errors import DeserializationError

OfferStateString: TypeAlias = Literal[
    "Draft",
    "Released",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Draft",
        "Released",
    )
)


def serialize_json(value: OfferStateString) -> str:
    return value


def deserialize_json(data: str) -> OfferStateString:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OfferStateString value: {data!r}")
    return cast(OfferStateString, data)
