"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SlotFilterOperator``."""

from typing import Literal, TypeAlias, cast

SlotFilterOperator: TypeAlias = Literal[
    "CO",
    "EQ",
]


# --- restJson1 ser/de ---
def serialize_json(value: SlotFilterOperator) -> str:
    return value


def deserialize_json(data: str) -> SlotFilterOperator:
    return cast(SlotFilterOperator, data)
