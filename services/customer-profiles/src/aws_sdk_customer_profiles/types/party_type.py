"""Generated from Smithy shape ``com.amazonaws.customerprofiles#PartyType``."""

from typing import Literal, TypeAlias, cast

PartyType: TypeAlias = Literal[
    "INDIVIDUAL",
    "BUSINESS",
    "OTHER",
]


# --- restJson1 ser/de ---
def serialize_json(value: PartyType) -> str:
    return value


def deserialize_json(data: str) -> PartyType:
    return cast(PartyType, data)
