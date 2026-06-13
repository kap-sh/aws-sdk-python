"""Generated from Smithy shape ``com.amazonaws.odb#AutonomousDatabaseResourceStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_odb.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_aws_json_1_0(value: AutonomousDatabaseResourceStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AutonomousDatabaseResourceStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AutonomousDatabaseResourceStatus value: {data!r}"
        )
    return cast(AutonomousDatabaseResourceStatus, data)
