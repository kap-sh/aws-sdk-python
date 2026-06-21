"""Generated from Smithy shape ``com.amazonaws.glue#CompressionType``."""

from typing import Literal, TypeAlias, cast

CompressionType: TypeAlias = Literal[
    "gzip",
    "bzip2",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CompressionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CompressionType:
    return cast(CompressionType, data)
