"""Generated from Smithy shape ``com.amazonaws.sagemaker#SchedulerResourceStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

SchedulerResourceStatus: TypeAlias = Literal[
    "Creating",
    "CreateFailed",
    "CreateRollbackFailed",
    "Created",
    "Updating",
    "UpdateFailed",
    "UpdateRollbackFailed",
    "Updated",
    "Deleting",
    "DeleteFailed",
    "DeleteRollbackFailed",
    "Deleted",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Creating",
        "CreateFailed",
        "CreateRollbackFailed",
        "Created",
        "Updating",
        "UpdateFailed",
        "UpdateRollbackFailed",
        "Updated",
        "Deleting",
        "DeleteFailed",
        "DeleteRollbackFailed",
        "Deleted",
    )
)


def serialize_aws_json_1_1(value: SchedulerResourceStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SchedulerResourceStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SchedulerResourceStatus value: {data!r}")
    return cast(SchedulerResourceStatus, data)
