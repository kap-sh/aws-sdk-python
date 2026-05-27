"""Generated from Smithy shape ``com.amazonaws.ecs#CapacityProviderType``."""

from typing import Literal, TypeAlias

CapacityProviderType: TypeAlias = Literal[
    "EC2_AUTOSCALING",
    "MANAGED_INSTANCES",
    "FARGATE",
    "FARGATE_SPOT",
]
