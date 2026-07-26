"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsTaskDefinitionContainerDefinitionsSecretsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_ecs_task_definition_container_definitions_secrets_details

AwsEcsTaskDefinitionContainerDefinitionsSecretsList: TypeAlias = list[
    "capo_securityhub.types.aws_ecs_task_definition_container_definitions_secrets_details.AwsEcsTaskDefinitionContainerDefinitionsSecretsDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsEcsTaskDefinitionContainerDefinitionsSecretsList) -> list:
    import capo_securityhub.types.aws_ecs_task_definition_container_definitions_secrets_details

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_ecs_task_definition_container_definitions_secrets_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsEcsTaskDefinitionContainerDefinitionsSecretsList:
    import capo_securityhub.types.aws_ecs_task_definition_container_definitions_secrets_details

    out: AwsEcsTaskDefinitionContainerDefinitionsSecretsList = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_ecs_task_definition_container_definitions_secrets_details.deserialize_json(
                item
            )
        )
    return out
