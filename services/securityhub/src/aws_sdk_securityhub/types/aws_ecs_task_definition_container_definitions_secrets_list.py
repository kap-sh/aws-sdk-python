"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsTaskDefinitionContainerDefinitionsSecretsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_ecs_task_definition_container_definitions_secrets_details

AwsEcsTaskDefinitionContainerDefinitionsSecretsList: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_ecs_task_definition_container_definitions_secrets_details.AwsEcsTaskDefinitionContainerDefinitionsSecretsDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsEcsTaskDefinitionContainerDefinitionsSecretsList) -> list:
    import aws_sdk_securityhub.types.aws_ecs_task_definition_container_definitions_secrets_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_ecs_task_definition_container_definitions_secrets_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsEcsTaskDefinitionContainerDefinitionsSecretsList:
    import aws_sdk_securityhub.types.aws_ecs_task_definition_container_definitions_secrets_details

    out: AwsEcsTaskDefinitionContainerDefinitionsSecretsList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_ecs_task_definition_container_definitions_secrets_details.deserialize_json(
                item
            )
        )
    return out
