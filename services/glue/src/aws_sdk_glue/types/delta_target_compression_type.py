"""Generated from Smithy shape ``com.amazonaws.glue#DeltaTargetCompressionType``."""

from typing import Literal, TypeAlias, cast

DeltaTargetCompressionType: TypeAlias = Literal[
    "uncompressed",
    "snappy",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeltaTargetCompressionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeltaTargetCompressionType:
    return cast(DeltaTargetCompressionType, data)
