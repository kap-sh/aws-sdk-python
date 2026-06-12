"""Generated from Smithy shape ``com.amazonaws.glue#FieldDataType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

FieldDataType: TypeAlias = Literal[
    "INT",
    "SMALLINT",
    "BIGINT",
    "FLOAT",
    "LONG",
    "DATE",
    "BOOLEAN",
    "MAP",
    "ARRAY",
    "STRING",
    "TIMESTAMP",
    "DECIMAL",
    "BYTE",
    "SHORT",
    "DOUBLE",
    "STRUCT",
    "BINARY",
    "UNION",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INT",
        "SMALLINT",
        "BIGINT",
        "FLOAT",
        "LONG",
        "DATE",
        "BOOLEAN",
        "MAP",
        "ARRAY",
        "STRING",
        "TIMESTAMP",
        "DECIMAL",
        "BYTE",
        "SHORT",
        "DOUBLE",
        "STRUCT",
        "BINARY",
        "UNION",
    )
)


def serialize_aws_json_1_1(value: FieldDataType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FieldDataType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FieldDataType value: {data!r}")
    return cast(FieldDataType, data)
