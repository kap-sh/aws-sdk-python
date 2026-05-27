"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonDeploymentStatus``."""

from typing import Literal, TypeAlias

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
