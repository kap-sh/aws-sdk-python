"""Generated from Smithy shape ``com.amazonaws.appconfig#DeploymentEventType``."""

from typing import Literal, TypeAlias, cast

DeploymentEventType: TypeAlias = Literal[
    "PERCENTAGE_UPDATED",
    "ROLLBACK_STARTED",
    "ROLLBACK_COMPLETED",
    "BAKE_TIME_STARTED",
    "DEPLOYMENT_STARTED",
    "DEPLOYMENT_COMPLETED",
    "REVERT_COMPLETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentEventType) -> str:
    return value


def deserialize_json(data: str) -> DeploymentEventType:
    return cast(DeploymentEventType, data)
