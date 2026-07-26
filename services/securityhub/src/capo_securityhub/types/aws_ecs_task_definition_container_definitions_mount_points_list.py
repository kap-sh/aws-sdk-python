"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsTaskDefinitionContainerDefinitionsMountPointsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_ecs_task_definition_container_definitions_mount_points_details

AwsEcsTaskDefinitionContainerDefinitionsMountPointsList: TypeAlias = list[
    "capo_securityhub.types.aws_ecs_task_definition_container_definitions_mount_points_details.AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetails"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEcsTaskDefinitionContainerDefinitionsMountPointsList,
) -> list:
    import capo_securityhub.types.aws_ecs_task_definition_container_definitions_mount_points_details

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_ecs_task_definition_container_definitions_mount_points_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> AwsEcsTaskDefinitionContainerDefinitionsMountPointsList:
    import capo_securityhub.types.aws_ecs_task_definition_container_definitions_mount_points_details

    out: AwsEcsTaskDefinitionContainerDefinitionsMountPointsList = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_ecs_task_definition_container_definitions_mount_points_details.deserialize_json(
                item
            )
        )
    return out
