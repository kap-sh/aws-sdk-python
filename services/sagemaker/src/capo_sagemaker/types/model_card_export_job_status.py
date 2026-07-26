"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelCardExportJobStatus``."""

from typing import Literal, TypeAlias, cast

ModelCardExportJobStatus: TypeAlias = Literal[
    "InProgress",
    "Completed",
    "Failed",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelCardExportJobStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ModelCardExportJobStatus:
    return cast(ModelCardExportJobStatus, data)
