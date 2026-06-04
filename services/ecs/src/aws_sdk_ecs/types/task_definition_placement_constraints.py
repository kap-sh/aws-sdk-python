"""Generated from Smithy shape ``com.amazonaws.ecs#TaskDefinitionPlacementConstraints``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.task_definition_placement_constraint

TaskDefinitionPlacementConstraints: TypeAlias = list[
    "aws_sdk_ecs.types.task_definition_placement_constraint.TaskDefinitionPlacementConstraint"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaskDefinitionPlacementConstraints) -> list:
    import aws_sdk_ecs.types.task_definition_placement_constraint

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ecs.types.task_definition_placement_constraint.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TaskDefinitionPlacementConstraints:
    import aws_sdk_ecs.types.task_definition_placement_constraint

    out: TaskDefinitionPlacementConstraints = []
    for item in data:
        out.append(
            aws_sdk_ecs.types.task_definition_placement_constraint.deserialize_aws_json_1_1(
                item
            )
        )
    return out
