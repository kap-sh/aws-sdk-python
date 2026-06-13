"""Generated from Smithy shape ``com.amazonaws.quicksight#ColumnRole``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

ColumnRole: TypeAlias = Literal[
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


def serialize_json(value: ColumnRole) -> str:
    return value


def deserialize_json(data: str) -> ColumnRole:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ColumnRole value: {data!r}")
    return cast(ColumnRole, data)
