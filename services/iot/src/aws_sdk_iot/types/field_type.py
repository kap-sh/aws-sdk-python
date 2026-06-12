"""Generated from Smithy shape ``com.amazonaws.iot#FieldType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

FieldType: TypeAlias = Literal[
    "Number",
    "String",
    "Boolean",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Number",
        "String",
        "Boolean",
    )
)


def serialize_json(value: FieldType) -> str:
    return value


def deserialize_json(data: str) -> FieldType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FieldType value: {data!r}")
    return cast(FieldType, data)
