"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListingMode``."""

from typing import Literal, TypeAlias, cast

ListingMode: TypeAlias = Literal[
    "DEFAULT",
    "DYNAMIC",
]


# --- restJson1 ser/de ---
def serialize_json(value: ListingMode) -> str:
    return value


def deserialize_json(data: str) -> ListingMode:
    return cast(ListingMode, data)
