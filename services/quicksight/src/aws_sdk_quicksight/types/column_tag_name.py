"""Generated from Smithy shape ``com.amazonaws.quicksight#ColumnTagName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

ColumnTagName: TypeAlias = Literal[
    "COLUMN_GEOGRAPHIC_ROLE",
    "COLUMN_DESCRIPTION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COLUMN_GEOGRAPHIC_ROLE",
        "COLUMN_DESCRIPTION",
    )
)


def serialize_json(value: ColumnTagName) -> str:
    return value


def deserialize_json(data: str) -> ColumnTagName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ColumnTagName value: {data!r}")
    return cast(ColumnTagName, data)
