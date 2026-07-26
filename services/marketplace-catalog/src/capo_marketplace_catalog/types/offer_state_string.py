"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#OfferStateString``."""

from typing import Literal, TypeAlias, cast

OfferStateString: TypeAlias = Literal[
    "Draft",
    "Released",
]


# --- restJson1 ser/de ---
def serialize_json(value: OfferStateString) -> str:
    return value


def deserialize_json(data: str) -> OfferStateString:
    return cast(OfferStateString, data)
