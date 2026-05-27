"""Generated from Smithy shape ``com.amazonaws.ecs#DeploymentStrategy``."""

from typing import Literal, TypeAlias

DeploymentStrategy: TypeAlias = Literal[
    "ROLLING",
    "BLUE_GREEN",
    "LINEAR",
    "CANARY",
]
