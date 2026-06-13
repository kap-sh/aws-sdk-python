"""Generated from Smithy shape ``com.amazonaws.quicksight#PivotTableMetricPlacement``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

PivotTableMetricPlacement: TypeAlias = Literal[
    "ROW",
    "COLUMN",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ROW",
        "COLUMN",
    )
)


def serialize_json(value: PivotTableMetricPlacement) -> str:
    return value


def deserialize_json(data: str) -> PivotTableMetricPlacement:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PivotTableMetricPlacement value: {data!r}")
    return cast(PivotTableMetricPlacement, data)
