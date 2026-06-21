"""Generated from Smithy shape ``com.amazonaws.datazone#DeploymentStatus``."""

from typing import Literal, TypeAlias, cast

DeploymentStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "SUCCESSFUL",
    "FAILED",
    "PENDING_DEPLOYMENT",
]


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentStatus) -> str:
    return value


def deserialize_json(data: str) -> DeploymentStatus:
    return cast(DeploymentStatus, data)
