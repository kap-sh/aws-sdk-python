"""Generated from Smithy shape ``com.amazonaws.quicksight#PivotTableRowsLayout``."""

from typing import Literal, TypeAlias, cast

PivotTableRowsLayout: TypeAlias = Literal[
    "TABULAR",
    "HIERARCHY",
]


# --- restJson1 ser/de ---
def serialize_json(value: PivotTableRowsLayout) -> str:
    return value


def deserialize_json(data: str) -> PivotTableRowsLayout:
    return cast(PivotTableRowsLayout, data)
