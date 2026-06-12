"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsTaskDefinitionContainerDefinitionsPortMappingsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_ecs_task_definition_container_definitions_port_mappings_details

AwsEcsTaskDefinitionContainerDefinitionsPortMappingsList: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_ecs_task_definition_container_definitions_port_mappings_details.AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetails"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEcsTaskDefinitionContainerDefinitionsPortMappingsList,
) -> list:
    import aws_sdk_securityhub.types.aws_ecs_task_definition_container_definitions_port_mappings_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_ecs_task_definition_container_definitions_port_mappings_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> AwsEcsTaskDefinitionContainerDefinitionsPortMappingsList:
    import aws_sdk_securityhub.types.aws_ecs_task_definition_container_definitions_port_mappings_details

    out: AwsEcsTaskDefinitionContainerDefinitionsPortMappingsList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_ecs_task_definition_container_definitions_port_mappings_details.deserialize_json(
                item
            )
        )
    return out
