"""Generated from Smithy shape ``com.amazonaws.glue#HudiTargetCompressionType``."""

from typing import Literal, TypeAlias, cast

HudiTargetCompressionType: TypeAlias = Literal[
    "gzip",
    "lzo",
    "uncompressed",
    "snappy",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HudiTargetCompressionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HudiTargetCompressionType:
    return cast(HudiTargetCompressionType, data)
