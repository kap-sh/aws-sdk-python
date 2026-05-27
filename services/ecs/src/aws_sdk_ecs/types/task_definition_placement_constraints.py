"""Generated from Smithy shape ``com.amazonaws.ecs#TaskDefinitionPlacementConstraints``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.task_definition_placement_constraint

TaskDefinitionPlacementConstraints: TypeAlias = list[
    "aws_sdk_ecs.types.task_definition_placement_constraint.TaskDefinitionPlacementConstraint"
]
