"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrackingServerStatus``."""

from typing import Literal, TypeAlias, cast

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
def serialize_aws_json_1_1(value: TrackingServerStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TrackingServerStatus:
    return cast(TrackingServerStatus, data)
