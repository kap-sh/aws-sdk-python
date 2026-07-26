"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#OfferTargetingString``."""

from typing import Literal, TypeAlias, cast

OfferTargetingString: TypeAlias = Literal[
    "BuyerAccounts",
    "ParticipatingPrograms",
    "CountryCodes",
    "None",
]


# --- restJson1 ser/de ---
def serialize_json(value: OfferTargetingString) -> str:
    return value


def deserialize_json(data: str) -> OfferTargetingString:
    return cast(OfferTargetingString, data)
