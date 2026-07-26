"""Generated from Smithy shape ``com.amazonaws.quicksight#PivotTableConditionalFormattingScopeRole``."""

from typing import Literal, TypeAlias, cast

PivotTableConditionalFormattingScopeRole: TypeAlias = Literal[
    "FIELD",
    "FIELD_TOTAL",
    "GRAND_TOTAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: PivotTableConditionalFormattingScopeRole) -> str:
    return value


def deserialize_json(data: str) -> PivotTableConditionalFormattingScopeRole:
    return cast(PivotTableConditionalFormattingScopeRole, data)
