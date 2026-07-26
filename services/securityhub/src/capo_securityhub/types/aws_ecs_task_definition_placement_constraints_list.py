"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsTaskDefinitionPlacementConstraintsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_ecs_task_definition_placement_constraints_details

AwsEcsTaskDefinitionPlacementConstraintsList: TypeAlias = list[
    "capo_securityhub.types.aws_ecs_task_definition_placement_constraints_details.AwsEcsTaskDefinitionPlacementConstraintsDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsEcsTaskDefinitionPlacementConstraintsList) -> list:
    import capo_securityhub.types.aws_ecs_task_definition_placement_constraints_details

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_ecs_task_definition_placement_constraints_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsEcsTaskDefinitionPlacementConstraintsList:
    import capo_securityhub.types.aws_ecs_task_definition_placement_constraints_details

    out: AwsEcsTaskDefinitionPlacementConstraintsList = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_ecs_task_definition_placement_constraints_details.deserialize_json(
                item
            )
        )
    return out
