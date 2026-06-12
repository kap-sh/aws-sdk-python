"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrainingJobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

TrainingJobStatus: TypeAlias = Literal[
    "InProgress",
    "Completed",
    "Failed",
    "Stopping",
    "Stopped",
    "Deleting",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "InProgress",
        "Completed",
        "Failed",
        "Stopping",
        "Stopped",
        "Deleting",
    )
)


def serialize_aws_json_1_1(value: TrainingJobStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TrainingJobStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TrainingJobStatus value: {data!r}")
    return cast(TrainingJobStatus, data)
