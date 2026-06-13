"""Generated from Smithy shape ``com.amazonaws.quicksight#PivotTableConditionalFormattingScopeRole``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

PivotTableConditionalFormattingScopeRole: TypeAlias = Literal[
    "FIELD",
    "FIELD_TOTAL",
    "GRAND_TOTAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FIELD",
        "FIELD_TOTAL",
        "GRAND_TOTAL",
    )
)


def serialize_json(value: PivotTableConditionalFormattingScopeRole) -> str:
    return value


def deserialize_json(data: str) -> PivotTableConditionalFormattingScopeRole:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown PivotTableConditionalFormattingScopeRole value: {data!r}"
        )
    return cast(PivotTableConditionalFormattingScopeRole, data)
