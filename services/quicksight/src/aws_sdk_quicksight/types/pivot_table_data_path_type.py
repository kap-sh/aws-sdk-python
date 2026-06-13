"""Generated from Smithy shape ``com.amazonaws.quicksight#PivotTableDataPathType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

PivotTableDataPathType: TypeAlias = Literal[
    "HIERARCHY_ROWS_LAYOUT_COLUMN",
    "MULTIPLE_ROW_METRICS_COLUMN",
    "EMPTY_COLUMN_HEADER",
    "COUNT_METRIC_COLUMN",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HIERARCHY_ROWS_LAYOUT_COLUMN",
        "MULTIPLE_ROW_METRICS_COLUMN",
        "EMPTY_COLUMN_HEADER",
        "COUNT_METRIC_COLUMN",
    )
)


def serialize_json(value: PivotTableDataPathType) -> str:
    return value


def deserialize_json(data: str) -> PivotTableDataPathType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PivotTableDataPathType value: {data!r}")
    return cast(PivotTableDataPathType, data)
