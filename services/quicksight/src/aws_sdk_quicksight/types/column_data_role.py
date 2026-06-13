"""Generated from Smithy shape ``com.amazonaws.quicksight#ColumnDataRole``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

ColumnDataRole: TypeAlias = Literal[
    "DIMENSION",
    "MEASURE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DIMENSION",
        "MEASURE",
    )
)


def serialize_json(value: ColumnDataRole) -> str:
    return value


def deserialize_json(data: str) -> ColumnDataRole:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ColumnDataRole value: {data!r}")
    return cast(ColumnDataRole, data)
