"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsTaskDefinitionPlacementConstraintsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_ecs_task_definition_placement_constraints_details

AwsEcsTaskDefinitionPlacementConstraintsList: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_ecs_task_definition_placement_constraints_details.AwsEcsTaskDefinitionPlacementConstraintsDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsEcsTaskDefinitionPlacementConstraintsList) -> list:
    import aws_sdk_securityhub.types.aws_ecs_task_definition_placement_constraints_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_ecs_task_definition_placement_constraints_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsEcsTaskDefinitionPlacementConstraintsList:
    import aws_sdk_securityhub.types.aws_ecs_task_definition_placement_constraints_details

    out: AwsEcsTaskDefinitionPlacementConstraintsList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_ecs_task_definition_placement_constraints_details.deserialize_json(
                item
            )
        )
    return out
