"""Generated from Smithy shape ``com.amazonaws.lambda#SchemaRegistryEventRecordFormat``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_lambda.errors import DeserializationError

SchemaRegistryEventRecordFormat: TypeAlias = Literal[
    "JSON",
    "SOURCE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "JSON",
        "SOURCE",
    )
)


def serialize_json(value: SchemaRegistryEventRecordFormat) -> str:
    return value


def deserialize_json(data: str) -> SchemaRegistryEventRecordFormat:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown SchemaRegistryEventRecordFormat value: {data!r}"
        )
    return cast(SchemaRegistryEventRecordFormat, data)
