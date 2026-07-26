"""Generated from Smithy shape ``com.amazonaws.glue#GlueRecordType``."""

from typing import Literal, TypeAlias, cast

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
def serialize_aws_json_1_1(value: GlueRecordType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> GlueRecordType:
    return cast(GlueRecordType, data)
