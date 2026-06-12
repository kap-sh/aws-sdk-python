"""Generated from Smithy shape ``com.amazonaws.sagemaker#HyperParameterTuningJobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

HyperParameterTuningJobStatus: TypeAlias = Literal[
    "Completed",
    "InProgress",
    "Failed",
    "Stopped",
    "Stopping",
    "Deleting",
    "DeleteFailed",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Completed",
        "InProgress",
        "Failed",
        "Stopped",
        "Stopping",
        "Deleting",
        "DeleteFailed",
    )
)


def serialize_aws_json_1_1(value: HyperParameterTuningJobStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HyperParameterTuningJobStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown HyperParameterTuningJobStatus value: {data!r}"
        )
    return cast(HyperParameterTuningJobStatus, data)
