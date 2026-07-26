"""Generated from Smithy shape ``com.amazonaws.quicksight#PivotTableSubtotalLevel``."""

from typing import Literal, TypeAlias, cast

PivotTableSubtotalLevel: TypeAlias = Literal[
    "ALL",
    "CUSTOM",
    "LAST",
]


# --- restJson1 ser/de ---
def serialize_json(value: PivotTableSubtotalLevel) -> str:
    return value


def deserialize_json(data: str) -> PivotTableSubtotalLevel:
    return cast(PivotTableSubtotalLevel, data)
