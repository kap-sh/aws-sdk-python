"""Generated from Smithy shape ``com.amazonaws.sagemaker#ProcessingJobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ProcessingJobStatus: TypeAlias = Literal[
    "InProgress",
    "Completed",
    "Failed",
    "Stopping",
    "Stopped",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "InProgress",
        "Completed",
        "Failed",
        "Stopping",
        "Stopped",
    )
)


def serialize_aws_json_1_1(value: ProcessingJobStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProcessingJobStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProcessingJobStatus value: {data!r}")
    return cast(ProcessingJobStatus, data)
