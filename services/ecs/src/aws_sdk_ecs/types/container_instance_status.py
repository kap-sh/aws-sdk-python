"""Generated from Smithy shape ``com.amazonaws.ecs#ContainerInstanceStatus``."""

from typing import Literal, TypeAlias

ContainerInstanceStatus: TypeAlias = Literal[
    "ACTIVE",
    "DRAINING",
    "REGISTERING",
    "DEREGISTERING",
    "REGISTRATION_FAILED",
]
