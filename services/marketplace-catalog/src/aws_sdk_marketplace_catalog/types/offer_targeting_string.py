"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#OfferTargetingString``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_marketplace_catalog.errors import DeserializationError

OfferTargetingString: TypeAlias = Literal[
    "BuyerAccounts",
    "ParticipatingPrograms",
    "CountryCodes",
    "None",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BuyerAccounts",
        "ParticipatingPrograms",
        "CountryCodes",
        "None",
    )
)


def serialize_json(value: OfferTargetingString) -> str:
    return value


def deserialize_json(data: str) -> OfferTargetingString:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OfferTargetingString value: {data!r}")
    return cast(OfferTargetingString, data)
