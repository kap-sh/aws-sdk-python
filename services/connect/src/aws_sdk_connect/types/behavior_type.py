"""Generated from Smithy shape ``com.amazonaws.connect#BehaviorType``."""

from typing import Literal, TypeAlias, cast

BehaviorType: TypeAlias = Literal[
    "ROUTE_CURRENT_CHANNEL_ONLY",
    "ROUTE_ANY_CHANNEL",
]


# --- restJson1 ser/de ---
def serialize_json(value: BehaviorType) -> str:
    return value


def deserialize_json(data: str) -> BehaviorType:
    return cast(BehaviorType, data)
