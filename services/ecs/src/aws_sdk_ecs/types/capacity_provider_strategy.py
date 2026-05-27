"""Generated from Smithy shape ``com.amazonaws.ecs#CapacityProviderStrategy``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.capacity_provider_strategy_item

CapacityProviderStrategy: TypeAlias = list[
    "aws_sdk_ecs.types.capacity_provider_strategy_item.CapacityProviderStrategyItem"
]
