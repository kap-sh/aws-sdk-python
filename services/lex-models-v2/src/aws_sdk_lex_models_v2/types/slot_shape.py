"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SlotShape``."""

from typing import Literal, TypeAlias, cast

SlotShape: TypeAlias = Literal[
    "Scalar",
    "List",
]


# --- restJson1 ser/de ---
def serialize_json(value: SlotShape) -> str:
    return value


def deserialize_json(data: str) -> SlotShape:
    return cast(SlotShape, data)
