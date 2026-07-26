"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SlotTypeFilterOperator``."""

from typing import Literal, TypeAlias, cast

SlotTypeFilterOperator: TypeAlias = Literal[
    "CO",
    "EQ",
]


# --- restJson1 ser/de ---
def serialize_json(value: SlotTypeFilterOperator) -> str:
    return value


def deserialize_json(data: str) -> SlotTypeFilterOperator:
    return cast(SlotTypeFilterOperator, data)
