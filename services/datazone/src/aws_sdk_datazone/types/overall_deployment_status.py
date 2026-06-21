"""Generated from Smithy shape ``com.amazonaws.datazone#OverallDeploymentStatus``."""

from typing import Literal, TypeAlias, cast

OverallDeploymentStatus: TypeAlias = Literal[
    "PENDING_DEPLOYMENT",
    "IN_PROGRESS",
    "SUCCESSFUL",
    "FAILED_VALIDATION",
    "FAILED_DEPLOYMENT",
]


# --- restJson1 ser/de ---
def serialize_json(value: OverallDeploymentStatus) -> str:
    return value


def deserialize_json(data: str) -> OverallDeploymentStatus:
    return cast(OverallDeploymentStatus, data)
