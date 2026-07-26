"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsTaskDefinitionContainerDefinitionsVolumesFromList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_ecs_task_definition_container_definitions_volumes_from_details

AwsEcsTaskDefinitionContainerDefinitionsVolumesFromList: TypeAlias = list[
    "capo_securityhub.types.aws_ecs_task_definition_container_definitions_volumes_from_details.AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetails"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEcsTaskDefinitionContainerDefinitionsVolumesFromList,
) -> list:
    import capo_securityhub.types.aws_ecs_task_definition_container_definitions_volumes_from_details

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_ecs_task_definition_container_definitions_volumes_from_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> AwsEcsTaskDefinitionContainerDefinitionsVolumesFromList:
    import capo_securityhub.types.aws_ecs_task_definition_container_definitions_volumes_from_details

    out: AwsEcsTaskDefinitionContainerDefinitionsVolumesFromList = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_ecs_task_definition_container_definitions_volumes_from_details.deserialize_json(
                item
            )
        )
    return out
