"""Generated from Smithy shape ``com.amazonaws.quicksight#PivotTableSubtotalLevel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

PivotTableSubtotalLevel: TypeAlias = Literal[
    "ALL",
    "CUSTOM",
    "LAST",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALL",
        "CUSTOM",
        "LAST",
    )
)


def serialize_json(value: PivotTableSubtotalLevel) -> str:
    return value


def deserialize_json(data: str) -> PivotTableSubtotalLevel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PivotTableSubtotalLevel value: {data!r}")
    return cast(PivotTableSubtotalLevel, data)
