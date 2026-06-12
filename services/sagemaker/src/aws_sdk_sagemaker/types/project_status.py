"""Generated from Smithy shape ``com.amazonaws.sagemaker#ProjectStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ProjectStatus: TypeAlias = Literal[
    "Pending",
    "CreateInProgress",
    "CreateCompleted",
    "CreateFailed",
    "DeleteInProgress",
    "DeleteFailed",
    "DeleteCompleted",
    "UpdateInProgress",
    "UpdateCompleted",
    "UpdateFailed",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Pending",
        "CreateInProgress",
        "CreateCompleted",
        "CreateFailed",
        "DeleteInProgress",
        "DeleteFailed",
        "DeleteCompleted",
        "UpdateInProgress",
        "UpdateCompleted",
        "UpdateFailed",
    )
)


def serialize_aws_json_1_1(value: ProjectStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProjectStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProjectStatus value: {data!r}")
    return cast(ProjectStatus, data)
