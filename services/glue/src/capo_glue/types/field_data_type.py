"""Generated from Smithy shape ``com.amazonaws.glue#FieldDataType``."""

from typing import Literal, TypeAlias, cast

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
def serialize_aws_json_1_1(value: FieldDataType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FieldDataType:
    return cast(FieldDataType, data)
