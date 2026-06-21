"""Generated from Smithy shape ``com.amazonaws.mediaconnect#BridgePlacement``."""

from typing import Literal, TypeAlias, cast

BridgePlacement: TypeAlias = Literal[
    "AVAILABLE",
    "LOCKED",
]


# --- restJson1 ser/de ---
def serialize_json(value: BridgePlacement) -> str:
    return value


def deserialize_json(data: str) -> BridgePlacement:
    return cast(BridgePlacement, data)
