"""Generated from Smithy shape ``com.amazonaws.quicksight#PivotTableDataPathType``."""

from typing import Literal, TypeAlias, cast

PivotTableDataPathType: TypeAlias = Literal[
    "HIERARCHY_ROWS_LAYOUT_COLUMN",
    "MULTIPLE_ROW_METRICS_COLUMN",
    "EMPTY_COLUMN_HEADER",
    "COUNT_METRIC_COLUMN",
]


# --- restJson1 ser/de ---
def serialize_json(value: PivotTableDataPathType) -> str:
    return value


def deserialize_json(data: str) -> PivotTableDataPathType:
    return cast(PivotTableDataPathType, data)
