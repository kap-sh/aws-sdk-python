"""Generated from Smithy shape ``com.amazonaws.ecs#PlacementConstraints``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.placement_constraint

PlacementConstraints: TypeAlias = list[
    "aws_sdk_ecs.types.placement_constraint.PlacementConstraint"
]
