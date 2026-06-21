"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#OwnershipType``."""

from typing import Literal, TypeAlias, cast

OwnershipType: TypeAlias = Literal[
    "SELF",
    "SHARED",
]


# --- restJson1 ser/de ---
def serialize_json(value: OwnershipType) -> str:
    return value


def deserialize_json(data: str) -> OwnershipType:
    return cast(OwnershipType, data)
