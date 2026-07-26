"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsTaskDefinitionContainerDefinitionsSystemControlsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_ecs_task_definition_container_definitions_system_controls_details

AwsEcsTaskDefinitionContainerDefinitionsSystemControlsList: TypeAlias = list[
    "capo_securityhub.types.aws_ecs_task_definition_container_definitions_system_controls_details.AwsEcsTaskDefinitionContainerDefinitionsSystemControlsDetails"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEcsTaskDefinitionContainerDefinitionsSystemControlsList,
) -> list:
    import capo_securityhub.types.aws_ecs_task_definition_container_definitions_system_controls_details

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_ecs_task_definition_container_definitions_system_controls_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> AwsEcsTaskDefinitionContainerDefinitionsSystemControlsList:
    import capo_securityhub.types.aws_ecs_task_definition_container_definitions_system_controls_details

    out: AwsEcsTaskDefinitionContainerDefinitionsSystemControlsList = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_ecs_task_definition_container_definitions_system_controls_details.deserialize_json(
                item
            )
        )
    return out
