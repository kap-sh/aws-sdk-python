"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsTaskDefinitionContainerDefinitionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_ecs_task_definition_container_definitions_details

AwsEcsTaskDefinitionContainerDefinitionsList: TypeAlias = list[
    "capo_securityhub.types.aws_ecs_task_definition_container_definitions_details.AwsEcsTaskDefinitionContainerDefinitionsDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsEcsTaskDefinitionContainerDefinitionsList) -> list:
    import capo_securityhub.types.aws_ecs_task_definition_container_definitions_details

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_ecs_task_definition_container_definitions_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsEcsTaskDefinitionContainerDefinitionsList:
    import capo_securityhub.types.aws_ecs_task_definition_container_definitions_details

    out: AwsEcsTaskDefinitionContainerDefinitionsList = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_ecs_task_definition_container_definitions_details.deserialize_json(
                item
            )
        )
    return out
