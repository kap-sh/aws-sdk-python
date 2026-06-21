"""Generated from Smithy shape ``com.amazonaws.glue#HyperTargetCompressionType``."""

from typing import Literal, TypeAlias, cast

HyperTargetCompressionType: TypeAlias = Literal["uncompressed",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HyperTargetCompressionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HyperTargetCompressionType:
    return cast(HyperTargetCompressionType, data)
