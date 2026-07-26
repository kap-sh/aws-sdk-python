"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsTaskDefinitionContainerDefinitionsPortMappingsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_ecs_task_definition_container_definitions_port_mappings_details

AwsEcsTaskDefinitionContainerDefinitionsPortMappingsList: TypeAlias = list[
    "capo_securityhub.types.aws_ecs_task_definition_container_definitions_port_mappings_details.AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetails"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEcsTaskDefinitionContainerDefinitionsPortMappingsList,
) -> list:
    import capo_securityhub.types.aws_ecs_task_definition_container_definitions_port_mappings_details

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_ecs_task_definition_container_definitions_port_mappings_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> AwsEcsTaskDefinitionContainerDefinitionsPortMappingsList:
    import capo_securityhub.types.aws_ecs_task_definition_container_definitions_port_mappings_details

    out: AwsEcsTaskDefinitionContainerDefinitionsPortMappingsList = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_ecs_task_definition_container_definitions_port_mappings_details.deserialize_json(
                item
            )
        )
    return out
