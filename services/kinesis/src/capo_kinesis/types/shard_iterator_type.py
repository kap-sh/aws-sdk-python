"""Generated from Smithy shape ``com.amazonaws.kinesis#ShardIteratorType``."""

from typing import Literal, TypeAlias, cast

ShardIteratorType: TypeAlias = Literal[
    "AT_SEQUENCE_NUMBER",
    "AFTER_SEQUENCE_NUMBER",
    "TRIM_HORIZON",
    "LATEST",
    "AT_TIMESTAMP",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ShardIteratorType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ShardIteratorType:
    return cast(ShardIteratorType, data)
