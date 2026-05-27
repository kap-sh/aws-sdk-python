"""Generated from Smithy shape ``com.amazonaws.ecs#DeploymentLifecycleHookStatus``."""

from typing import Literal, TypeAlias

DeploymentLifecycleHookStatus: TypeAlias = Literal[
    "AWAITING_ACTION",
    "IN_PROGRESS",
    "SUCCEEDED",
    "FAILED",
    "TIMED_OUT",
]
