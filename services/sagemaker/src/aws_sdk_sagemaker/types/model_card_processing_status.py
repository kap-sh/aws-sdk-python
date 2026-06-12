"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelCardProcessingStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ModelCardProcessingStatus: TypeAlias = Literal[
    "DeleteInProgress",
    "DeletePending",
    "ContentDeleted",
    "ExportJobsDeleted",
    "DeleteCompleted",
    "DeleteFailed",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DeleteInProgress",
        "DeletePending",
        "ContentDeleted",
        "ExportJobsDeleted",
        "DeleteCompleted",
        "DeleteFailed",
    )
)


def serialize_aws_json_1_1(value: ModelCardProcessingStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ModelCardProcessingStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ModelCardProcessingStatus value: {data!r}")
    return cast(ModelCardProcessingStatus, data)
