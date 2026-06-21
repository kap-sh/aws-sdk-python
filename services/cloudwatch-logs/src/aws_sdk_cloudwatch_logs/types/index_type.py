"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#IndexType``."""

from typing import Literal, TypeAlias, cast

IndexType: TypeAlias = Literal[
    "FACET",
    "FIELD_INDEX",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IndexType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IndexType:
    return cast(IndexType, data)
