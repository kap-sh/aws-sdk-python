"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelCardProcessingStatus``."""

from typing import Literal, TypeAlias, cast

ModelCardProcessingStatus: TypeAlias = Literal[
    "DeleteInProgress",
    "DeletePending",
    "ContentDeleted",
    "ExportJobsDeleted",
    "DeleteCompleted",
    "DeleteFailed",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelCardProcessingStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ModelCardProcessingStatus:
    return cast(ModelCardProcessingStatus, data)
