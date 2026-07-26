"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SlotResolutionStrategy``."""

from typing import Literal, TypeAlias, cast

SlotResolutionStrategy: TypeAlias = Literal[
    "EnhancedFallback",
    "Default",
]


# --- restJson1 ser/de ---
def serialize_json(value: SlotResolutionStrategy) -> str:
    return value


def deserialize_json(data: str) -> SlotResolutionStrategy:
    return cast(SlotResolutionStrategy, data)
