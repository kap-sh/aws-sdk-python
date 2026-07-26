"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonDeploymentStatus``."""

from typing import Literal, TypeAlias, cast

DaemonDeploymentStatus: TypeAlias = Literal[
    "PENDING",
    "SUCCESSFUL",
    "STOPPED",
    "STOP_REQUESTED",
    "IN_PROGRESS",
    "ROLLBACK_IN_PROGRESS",
    "ROLLBACK_SUCCESSFUL",
    "ROLLBACK_FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DaemonDeploymentStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DaemonDeploymentStatus:
    return cast(DaemonDeploymentStatus, data)
