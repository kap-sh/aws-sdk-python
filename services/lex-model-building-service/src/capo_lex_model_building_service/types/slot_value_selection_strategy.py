"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#SlotValueSelectionStrategy``."""

from typing import Literal, TypeAlias, cast

SlotValueSelectionStrategy: TypeAlias = Literal[
    "ORIGINAL_VALUE",
    "TOP_RESOLUTION",
]


# --- restJson1 ser/de ---
def serialize_json(value: SlotValueSelectionStrategy) -> str:
    return value


def deserialize_json(data: str) -> SlotValueSelectionStrategy:
    return cast(SlotValueSelectionStrategy, data)
