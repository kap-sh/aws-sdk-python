"""Generated from Smithy shape ``com.amazonaws.quicksight#DisplayFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

DisplayFormat: TypeAlias = Literal[
    "AUTO",
    "PERCENT",
    "CURRENCY",
    "NUMBER",
    "DATE",
    "STRING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUTO",
        "PERCENT",
        "CURRENCY",
        "NUMBER",
        "DATE",
        "STRING",
    )
)


def serialize_json(value: DisplayFormat) -> str:
    return value


def deserialize_json(data: str) -> DisplayFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DisplayFormat value: {data!r}")
    return cast(DisplayFormat, data)
