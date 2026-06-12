"""Generated from Smithy shape ``com.amazonaws.rekognition#ProjectVersionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rekognition.errors import DeserializationError

ProjectVersionStatus: TypeAlias = Literal[
    "TRAINING_IN_PROGRESS",
    "TRAINING_COMPLETED",
    "TRAINING_FAILED",
    "STARTING",
    "RUNNING",
    "FAILED",
    "STOPPING",
    "STOPPED",
    "DELETING",
    "COPYING_IN_PROGRESS",
    "COPYING_COMPLETED",
    "COPYING_FAILED",
    "DEPRECATED",
    "EXPIRED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TRAINING_IN_PROGRESS",
        "TRAINING_COMPLETED",
        "TRAINING_FAILED",
        "STARTING",
        "RUNNING",
        "FAILED",
        "STOPPING",
        "STOPPED",
        "DELETING",
        "COPYING_IN_PROGRESS",
        "COPYING_COMPLETED",
        "COPYING_FAILED",
        "DEPRECATED",
        "EXPIRED",
    )
)


def serialize_aws_json_1_1(value: ProjectVersionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProjectVersionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProjectVersionStatus value: {data!r}")
    return cast(ProjectVersionStatus, data)
