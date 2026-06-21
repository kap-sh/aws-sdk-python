"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#SlotConstraint``."""

from typing import Literal, TypeAlias, cast

SlotConstraint: TypeAlias = Literal[
    "Required",
    "Optional",
]


# --- restJson1 ser/de ---
def serialize_json(value: SlotConstraint) -> str:
    return value


def deserialize_json(data: str) -> SlotConstraint:
    return cast(SlotConstraint, data)
