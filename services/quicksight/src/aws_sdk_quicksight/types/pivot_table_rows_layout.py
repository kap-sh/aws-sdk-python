"""Generated from Smithy shape ``com.amazonaws.quicksight#PivotTableRowsLayout``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

PivotTableRowsLayout: TypeAlias = Literal[
    "TABULAR",
    "HIERARCHY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TABULAR",
        "HIERARCHY",
    )
)


def serialize_json(value: PivotTableRowsLayout) -> str:
    return value


def deserialize_json(data: str) -> PivotTableRowsLayout:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PivotTableRowsLayout value: {data!r}")
    return cast(PivotTableRowsLayout, data)
