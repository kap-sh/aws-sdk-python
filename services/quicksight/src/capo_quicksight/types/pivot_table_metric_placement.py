"""Generated from Smithy shape ``com.amazonaws.quicksight#PivotTableMetricPlacement``."""

from typing import Literal, TypeAlias, cast

PivotTableMetricPlacement: TypeAlias = Literal[
    "ROW",
    "COLUMN",
]


# --- restJson1 ser/de ---
def serialize_json(value: PivotTableMetricPlacement) -> str:
    return value


def deserialize_json(data: str) -> PivotTableMetricPlacement:
    return cast(PivotTableMetricPlacement, data)
