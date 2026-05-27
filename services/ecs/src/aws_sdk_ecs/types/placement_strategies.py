"""Generated from Smithy shape ``com.amazonaws.ecs#PlacementStrategies``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.placement_strategy

PlacementStrategies: TypeAlias = list[
    "aws_sdk_ecs.types.placement_strategy.PlacementStrategy"
]
