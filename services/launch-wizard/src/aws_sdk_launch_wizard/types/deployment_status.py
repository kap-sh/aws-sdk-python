"""Generated from Smithy shape ``com.amazonaws.launchwizard#DeploymentStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_launch_wizard.errors import DeserializationError

DeploymentStatus: TypeAlias = Literal[
    "COMPLETED",
    "CREATING",
    "DELETE_IN_PROGRESS",
    "DELETE_INITIATING",
    "DELETE_FAILED",
    "DELETED",
    "FAILED",
    "IN_PROGRESS",
    "VALIDATING",
    "UPDATE_IN_PROGRESS",
    "UPDATE_COMPLETED",
    "UPDATE_FAILED",
    "UPDATE_ROLLBACK_COMPLETED",
    "UPDATE_ROLLBACK_FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COMPLETED",
        "CREATING",
        "DELETE_IN_PROGRESS",
        "DELETE_INITIATING",
        "DELETE_FAILED",
        "DELETED",
        "FAILED",
        "IN_PROGRESS",
        "VALIDATING",
        "UPDATE_IN_PROGRESS",
        "UPDATE_COMPLETED",
        "UPDATE_FAILED",
        "UPDATE_ROLLBACK_COMPLETED",
        "UPDATE_ROLLBACK_FAILED",
    )
)


def serialize_json(value: DeploymentStatus) -> str:
    return value


def deserialize_json(data: str) -> DeploymentStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeploymentStatus value: {data!r}")
    return cast(DeploymentStatus, data)
