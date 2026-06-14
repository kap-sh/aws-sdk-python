"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkspaceState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces.errors import DeserializationError

WorkspaceState: TypeAlias = Literal[
    "PENDING",
    "AVAILABLE",
    "IMPAIRED",
    "UNHEALTHY",
    "REBOOTING",
    "STARTING",
    "REBUILDING",
    "RESTORING",
    "MAINTENANCE",
    "ADMIN_MAINTENANCE",
    "TERMINATING",
    "TERMINATED",
    "SUSPENDED",
    "UPDATING",
    "STOPPING",
    "STOPPED",
    "ERROR",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "AVAILABLE",
        "IMPAIRED",
        "UNHEALTHY",
        "REBOOTING",
        "STARTING",
        "REBUILDING",
        "RESTORING",
        "MAINTENANCE",
        "ADMIN_MAINTENANCE",
        "TERMINATING",
        "TERMINATED",
        "SUSPENDED",
        "UPDATING",
        "STOPPING",
        "STOPPED",
        "ERROR",
    )
)


def serialize_aws_json_1_1(value: WorkspaceState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WorkspaceState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WorkspaceState value: {data!r}")
    return cast(WorkspaceState, data)
