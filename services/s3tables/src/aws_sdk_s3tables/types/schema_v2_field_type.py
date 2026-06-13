"""Generated from Smithy shape ``com.amazonaws.s3tables#SchemaV2FieldType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3tables.errors import DeserializationError

SchemaV2FieldType: TypeAlias = Literal["struct",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("struct",))


def serialize_json(value: SchemaV2FieldType) -> str:
    return value


def deserialize_json(data: str) -> SchemaV2FieldType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SchemaV2FieldType value: {data!r}")
    return cast(SchemaV2FieldType, data)
