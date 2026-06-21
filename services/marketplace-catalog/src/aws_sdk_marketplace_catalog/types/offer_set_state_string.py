"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#OfferSetStateString``."""

from typing import Literal, TypeAlias, cast

OfferSetStateString: TypeAlias = Literal[
    "Draft",
    "Released",
]


# --- restJson1 ser/de ---
def serialize_json(value: OfferSetStateString) -> str:
    return value


def deserialize_json(data: str) -> OfferSetStateString:
    return cast(OfferSetStateString, data)
