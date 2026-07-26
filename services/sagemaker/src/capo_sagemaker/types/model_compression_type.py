"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelCompressionType``."""

from typing import Literal, TypeAlias, cast

ModelCompressionType: TypeAlias = Literal[
    "None",
    "Gzip",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelCompressionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ModelCompressionType:
    return cast(ModelCompressionType, data)
