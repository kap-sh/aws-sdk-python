"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SlotValueResolutionStrategy``."""

from typing import Literal, TypeAlias, cast

SlotValueResolutionStrategy: TypeAlias = Literal[
    "OriginalValue",
    "TopResolution",
    "Concatenation",
]


# --- restJson1 ser/de ---
def serialize_json(value: SlotValueResolutionStrategy) -> str:
    return value


def deserialize_json(data: str) -> SlotValueResolutionStrategy:
    return cast(SlotValueResolutionStrategy, data)
