"""Generated from Smithy shape ``com.amazonaws.sagemaker#InferenceExperimentStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

InferenceExperimentStatus: TypeAlias = Literal[
    "Creating",
    "Created",
    "Updating",
    "Running",
    "Starting",
    "Stopping",
    "Completed",
    "Cancelled",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Creating",
        "Created",
        "Updating",
        "Running",
        "Starting",
        "Stopping",
        "Completed",
        "Cancelled",
    )
)


def serialize_aws_json_1_1(value: InferenceExperimentStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InferenceExperimentStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InferenceExperimentStatus value: {data!r}")
    return cast(InferenceExperimentStatus, data)
