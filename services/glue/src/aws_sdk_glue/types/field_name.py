"""Generated from Smithy shape ``com.amazonaws.glue#FieldName``."""

from typing import Literal, TypeAlias, cast

FieldName: TypeAlias = Literal[
    "CRAWL_ID",
    "STATE",
    "START_TIME",
    "END_TIME",
    "DPU_HOUR",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FieldName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FieldName:
    return cast(FieldName, data)
