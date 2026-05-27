"""Generated from Smithy shape ``com.amazonaws.ecs#ManagedResourceStatus``."""

from typing import Literal, TypeAlias

ManagedResourceStatus: TypeAlias = Literal[
    "PROVISIONING",
    "ACTIVE",
    "DEPROVISIONING",
    "DELETED",
    "FAILED",
]
