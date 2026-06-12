"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_ecs_task_definition_proxy_configuration_proxy_configuration_properties_details

AwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesList: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_ecs_task_definition_proxy_configuration_proxy_configuration_properties_details.AwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesDetails"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesList,
) -> list:
    import aws_sdk_securityhub.types.aws_ecs_task_definition_proxy_configuration_proxy_configuration_properties_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_ecs_task_definition_proxy_configuration_proxy_configuration_properties_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> AwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesList:
    import aws_sdk_securityhub.types.aws_ecs_task_definition_proxy_configuration_proxy_configuration_properties_details

    out: AwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_ecs_task_definition_proxy_configuration_proxy_configuration_properties_details.deserialize_json(
                item
            )
        )
    return out
