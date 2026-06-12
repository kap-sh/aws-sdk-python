"""Generated from Smithy shape ``com.amazonaws.sagemaker#LabelingJobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

LabelingJobStatus: TypeAlias = Literal[
    "Initializing",
    "InProgress",
    "Completed",
    "Failed",
    "Stopping",
    "Stopped",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Initializing",
        "InProgress",
        "Completed",
        "Failed",
        "Stopping",
        "Stopped",
    )
)


def serialize_aws_json_1_1(value: LabelingJobStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LabelingJobStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LabelingJobStatus value: {data!r}")
    return cast(LabelingJobStatus, data)
