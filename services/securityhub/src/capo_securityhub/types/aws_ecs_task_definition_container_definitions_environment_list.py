"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsTaskDefinitionContainerDefinitionsEnvironmentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_ecs_task_definition_container_definitions_environment_details

AwsEcsTaskDefinitionContainerDefinitionsEnvironmentList: TypeAlias = list[
    "capo_securityhub.types.aws_ecs_task_definition_container_definitions_environment_details.AwsEcsTaskDefinitionContainerDefinitionsEnvironmentDetails"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEcsTaskDefinitionContainerDefinitionsEnvironmentList,
) -> list:
    import capo_securityhub.types.aws_ecs_task_definition_container_definitions_environment_details

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_ecs_task_definition_container_definitions_environment_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> AwsEcsTaskDefinitionContainerDefinitionsEnvironmentList:
    import capo_securityhub.types.aws_ecs_task_definition_container_definitions_environment_details

    out: AwsEcsTaskDefinitionContainerDefinitionsEnvironmentList = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_ecs_task_definition_container_definitions_environment_details.deserialize_json(
                item
            )
        )
    return out
