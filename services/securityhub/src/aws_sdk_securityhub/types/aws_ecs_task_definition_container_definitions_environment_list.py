"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsTaskDefinitionContainerDefinitionsEnvironmentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_ecs_task_definition_container_definitions_environment_details

AwsEcsTaskDefinitionContainerDefinitionsEnvironmentList: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_ecs_task_definition_container_definitions_environment_details.AwsEcsTaskDefinitionContainerDefinitionsEnvironmentDetails"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEcsTaskDefinitionContainerDefinitionsEnvironmentList,
) -> list:
    import aws_sdk_securityhub.types.aws_ecs_task_definition_container_definitions_environment_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_ecs_task_definition_container_definitions_environment_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> AwsEcsTaskDefinitionContainerDefinitionsEnvironmentList:
    import aws_sdk_securityhub.types.aws_ecs_task_definition_container_definitions_environment_details

    out: AwsEcsTaskDefinitionContainerDefinitionsEnvironmentList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_ecs_task_definition_container_definitions_environment_details.deserialize_json(
                item
            )
        )
    return out
