"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#DeploymentStatus``."""

from typing import Literal, TypeAlias, cast

DeploymentStatus: TypeAlias = Literal[
    "PENDING_UPDATE",
    "IN_PROGRESS",
    "COMPLETED",
    "NOT_ELIGIBLE",
    "ELIGIBLE",
]


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentStatus) -> str:
    return value


def deserialize_json(data: str) -> DeploymentStatus:
    return cast(DeploymentStatus, data)
