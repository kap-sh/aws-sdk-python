"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#OfferSetStateString``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_marketplace_catalog.errors import DeserializationError

OfferSetStateString: TypeAlias = Literal[
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


def serialize_json(value: OfferSetStateString) -> str:
    return value


def deserialize_json(data: str) -> OfferSetStateString:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OfferSetStateString value: {data!r}")
    return cast(OfferSetStateString, data)
