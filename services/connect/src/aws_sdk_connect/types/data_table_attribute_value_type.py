"""Generated from Smithy shape ``com.amazonaws.connect#DataTableAttributeValueType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

DataTableAttributeValueType: TypeAlias = Literal[
    "TEXT",
    "NUMBER",
    "BOOLEAN",
    "TEXT_LIST",
    "NUMBER_LIST",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TEXT",
        "NUMBER",
        "BOOLEAN",
        "TEXT_LIST",
        "NUMBER_LIST",
    )
)


def serialize_json(value: DataTableAttributeValueType) -> str:
    return value


def deserialize_json(data: str) -> DataTableAttributeValueType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DataTableAttributeValueType value: {data!r}"
        )
    return cast(DataTableAttributeValueType, data)
