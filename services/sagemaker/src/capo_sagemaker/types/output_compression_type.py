"""Generated from Smithy shape ``com.amazonaws.sagemaker#OutputCompressionType``."""

from typing import Literal, TypeAlias, cast

OutputCompressionType: TypeAlias = Literal[
    "GZIP",
    "NONE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OutputCompressionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OutputCompressionType:
    return cast(OutputCompressionType, data)
