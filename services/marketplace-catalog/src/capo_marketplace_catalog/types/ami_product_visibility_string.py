"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#AmiProductVisibilityString``."""

from typing import Literal, TypeAlias, cast

AmiProductVisibilityString: TypeAlias = Literal[
    "Limited",
    "Public",
    "Restricted",
    "Draft",
]


# --- restJson1 ser/de ---
def serialize_json(value: AmiProductVisibilityString) -> str:
    return value


def deserialize_json(data: str) -> AmiProductVisibilityString:
    return cast(AmiProductVisibilityString, data)
