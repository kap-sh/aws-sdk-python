"""Generated from Smithy shape ``com.amazonaws.quicksight#TableBorderStyle``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

TableBorderStyle: TypeAlias = Literal[
    "NONE",
    "SOLID",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "SOLID",
    )
)


def serialize_json(value: TableBorderStyle) -> str:
    return value


def deserialize_json(data: str) -> TableBorderStyle:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TableBorderStyle value: {data!r}")
    return cast(TableBorderStyle, data)
