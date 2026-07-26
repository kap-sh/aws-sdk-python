"""Generated from Smithy shape ``com.amazonaws.greengrass#BulkDeploymentStatus``."""

from typing import Literal, TypeAlias, cast

"""The current status of the bulk deployment."""
BulkDeploymentStatus: TypeAlias = Literal[
    "Initializing",
    "Running",
    "Completed",
    "Stopping",
    "Stopped",
    "Failed",
]


# --- restJson1 ser/de ---
def serialize_json(value: BulkDeploymentStatus) -> str:
    return value


def deserialize_json(data: str) -> BulkDeploymentStatus:
    return cast(BulkDeploymentStatus, data)
