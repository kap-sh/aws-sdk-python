"""Generated from Smithy shape ``com.amazonaws.ecs#LaunchType``."""

from typing import Literal, TypeAlias

LaunchType: TypeAlias = Literal[
    "EC2",
    "FARGATE",
    "EXTERNAL",
    "MANAGED_INSTANCES",
]
