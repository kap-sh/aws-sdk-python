"""Generated from Smithy shape ``com.amazonaws.odb#AutonomousDatabaseResourceStatus``."""

from typing import Literal, TypeAlias, cast

AutonomousDatabaseResourceStatus: TypeAlias = Literal[
    "AVAILABLE",
    "FAILED",
    "PROVISIONING",
    "TERMINATED",
    "TERMINATING",
    "UPDATING",
    "MAINTENANCE_IN_PROGRESS",
    "STOPPING",
    "STOPPED",
    "STARTING",
    "UNAVAILABLE",
    "RESTORE_IN_PROGRESS",
    "RESTORE_FAILED",
    "BACKUP_IN_PROGRESS",
    "SCALE_IN_PROGRESS",
    "AVAILABLE_NEEDS_ATTENTION",
    "RESTARTING",
    "RECREATING",
    "ROLE_CHANGE_IN_PROGRESS",
    "UPGRADING",
    "INACCESSIBLE",
    "STANDBY",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AutonomousDatabaseResourceStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AutonomousDatabaseResourceStatus:
    return cast(AutonomousDatabaseResourceStatus, data)
