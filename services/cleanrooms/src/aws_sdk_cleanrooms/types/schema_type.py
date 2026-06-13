"""Generated from Smithy shape ``com.amazonaws.cleanrooms#SchemaType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cleanrooms.errors import DeserializationError

SchemaType: TypeAlias = Literal[
    "TABLE",
    "ID_MAPPING_TABLE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TABLE",
        "ID_MAPPING_TABLE",
    )
)


def serialize_json(value: SchemaType) -> str:
    return value


def deserialize_json(data: str) -> SchemaType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SchemaType value: {data!r}")
    return cast(SchemaType, data)
