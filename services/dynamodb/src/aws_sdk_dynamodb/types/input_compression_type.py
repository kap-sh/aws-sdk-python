"""Generated from Smithy shape ``com.amazonaws.dynamodb#InputCompressionType``."""

from typing import Literal, TypeAlias, cast

InputCompressionType: TypeAlias = Literal[
    "GZIP",
    "ZSTD",
    "NONE",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InputCompressionType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> InputCompressionType:
    return cast(InputCompressionType, data)
