"""Generated from Smithy shape ``com.amazonaws.ecs#CapacityProviders``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.capacity_provider

CapacityProviders: TypeAlias = list[
    "aws_sdk_ecs.types.capacity_provider.CapacityProvider"
]
