"""Generated from Smithy shape ``com.amazonaws.mediatailor#Tier``."""

from typing import Literal, TypeAlias, cast

Tier: TypeAlias = Literal[
    "BASIC",
    "STANDARD",
]


# --- restJson1 ser/de ---
def serialize_json(value: Tier) -> str:
    return value


def deserialize_json(data: str) -> Tier:
    return cast(Tier, data)
