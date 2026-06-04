"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonDeploymentStatus``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ecs.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "SUCCESSFUL",
        "STOPPED",
        "STOP_REQUESTED",
        "IN_PROGRESS",
        "ROLLBACK_IN_PROGRESS",
        "ROLLBACK_SUCCESSFUL",
        "ROLLBACK_FAILED",
    )
)


def serialize_aws_json_1_1(value: DaemonDeploymentStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DaemonDeploymentStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DaemonDeploymentStatus value: {data!r}")
    return cast(DaemonDeploymentStatus, data)
