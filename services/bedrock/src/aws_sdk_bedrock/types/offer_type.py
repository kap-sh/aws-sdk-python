"""Generated from Smithy shape ``com.amazonaws.bedrock#OfferType``."""

from typing import Literal, TypeAlias, cast

OfferType: TypeAlias = Literal[
    "ALL",
    "PUBLIC",
]


# --- restJson1 ser/de ---
def serialize_json(value: OfferType) -> str:
    return value


def deserialize_json(data: str) -> OfferType:
    return cast(OfferType, data)
