"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsTaskDefinitionContainerDefinitionsUlimitsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_ecs_task_definition_container_definitions_ulimits_details

AwsEcsTaskDefinitionContainerDefinitionsUlimitsList: TypeAlias = list[
    "capo_securityhub.types.aws_ecs_task_definition_container_definitions_ulimits_details.AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsEcsTaskDefinitionContainerDefinitionsUlimitsList) -> list:
    import capo_securityhub.types.aws_ecs_task_definition_container_definitions_ulimits_details

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_ecs_task_definition_container_definitions_ulimits_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsEcsTaskDefinitionContainerDefinitionsUlimitsList:
    import capo_securityhub.types.aws_ecs_task_definition_container_definitions_ulimits_details

    out: AwsEcsTaskDefinitionContainerDefinitionsUlimitsList = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_ecs_task_definition_container_definitions_ulimits_details.deserialize_json(
                item
            )
        )
    return out
