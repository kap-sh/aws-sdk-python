"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelMetadataFilterType``."""

from typing import Literal, TypeAlias, cast

ModelMetadataFilterType: TypeAlias = Literal[
    "Domain",
    "Framework",
    "Task",
    "FrameworkVersion",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelMetadataFilterType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ModelMetadataFilterType:
    return cast(ModelMetadataFilterType, data)
