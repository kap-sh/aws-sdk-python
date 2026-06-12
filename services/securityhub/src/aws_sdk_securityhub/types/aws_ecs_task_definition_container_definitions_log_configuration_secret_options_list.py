"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationSecretOptionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_ecs_task_definition_container_definitions_log_configuration_secret_options_details

AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationSecretOptionsList: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_ecs_task_definition_container_definitions_log_configuration_secret_options_details.AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationSecretOptionsDetails"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationSecretOptionsList,
) -> list:
    import aws_sdk_securityhub.types.aws_ecs_task_definition_container_definitions_log_configuration_secret_options_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_ecs_task_definition_container_definitions_log_configuration_secret_options_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationSecretOptionsList:
    import aws_sdk_securityhub.types.aws_ecs_task_definition_container_definitions_log_configuration_secret_options_details

    out: AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationSecretOptionsList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_ecs_task_definition_container_definitions_log_configuration_secret_options_details.deserialize_json(
                item
            )
        )
    return out
