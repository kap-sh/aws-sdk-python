"""Generated from Smithy shape ``com.amazonaws.iotsitewise#WarmTierState``."""

from typing import Literal, TypeAlias, cast

WarmTierState: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: WarmTierState) -> str:
    return value


def deserialize_json(data: str) -> WarmTierState:
    return cast(WarmTierState, data)
