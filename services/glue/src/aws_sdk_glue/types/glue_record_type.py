"""Generated from Smithy shape ``com.amazonaws.glue#GlueRecordType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

GlueRecordType: TypeAlias = Literal[
    "DATE",
    "STRING",
    "TIMESTAMP",
    "INT",
    "FLOAT",
    "LONG",
    "BIGDECIMAL",
    "BYTE",
    "SHORT",
    "DOUBLE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DATE",
        "STRING",
        "TIMESTAMP",
        "INT",
        "FLOAT",
        "LONG",
        "BIGDECIMAL",
        "BYTE",
        "SHORT",
        "DOUBLE",
    )
)


def serialize_aws_json_1_1(value: GlueRecordType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> GlueRecordType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GlueRecordType value: {data!r}")
    return cast(GlueRecordType, data)
