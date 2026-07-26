"""Generated from Smithy shape ``com.amazonaws.repostspace#TierLevel``."""

from typing import Literal, TypeAlias, cast

TierLevel: TypeAlias = Literal[
    "BASIC",
    "STANDARD",
]


# --- restJson1 ser/de ---
def serialize_json(value: TierLevel) -> str:
    return value


def deserialize_json(data: str) -> TierLevel:
    return cast(TierLevel, data)
