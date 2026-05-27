"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceDeploymentStatus``."""

from typing import Literal, TypeAlias

ServiceDeploymentStatus: TypeAlias = Literal[
    "PENDING",
    "SUCCESSFUL",
    "STOPPED",
    "STOP_REQUESTED",
    "IN_PROGRESS",
    "ROLLBACK_REQUESTED",
    "ROLLBACK_IN_PROGRESS",
    "ROLLBACK_SUCCESSFUL",
    "ROLLBACK_FAILED",
]
