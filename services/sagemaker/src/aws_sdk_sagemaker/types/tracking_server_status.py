"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrackingServerStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

TrackingServerStatus: TypeAlias = Literal[
    "Creating",
    "Created",
    "CreateFailed",
    "Updating",
    "Updated",
    "UpdateFailed",
    "Deleting",
    "DeleteFailed",
    "Stopping",
    "Stopped",
    "StopFailed",
    "Starting",
    "Started",
    "StartFailed",
    "MaintenanceInProgress",
    "MaintenanceComplete",
    "MaintenanceFailed",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Creating",
        "Created",
        "CreateFailed",
        "Updating",
        "Updated",
        "UpdateFailed",
        "Deleting",
        "DeleteFailed",
        "Stopping",
        "Stopped",
        "StopFailed",
        "Starting",
        "Started",
        "StartFailed",
        "MaintenanceInProgress",
        "MaintenanceComplete",
        "MaintenanceFailed",
    )
)


def serialize_aws_json_1_1(value: TrackingServerStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TrackingServerStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TrackingServerStatus value: {data!r}")
    return cast(TrackingServerStatus, data)
