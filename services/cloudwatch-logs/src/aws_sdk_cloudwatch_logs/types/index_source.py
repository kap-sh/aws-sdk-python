"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#IndexSource``."""

from typing import Literal, TypeAlias, cast

IndexSource: TypeAlias = Literal[
    "ACCOUNT",
    "LOG_GROUP",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IndexSource) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IndexSource:
    return cast(IndexSource, data)
