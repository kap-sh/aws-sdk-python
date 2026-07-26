"""Generated from Smithy shape ``com.amazonaws.launchwizard#DeploymentStatus``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: DeploymentStatus) -> str:
    return value


def deserialize_json(data: str) -> DeploymentStatus:
    return cast(DeploymentStatus, data)
