"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_ecs_task_definition_proxy_configuration_proxy_configuration_properties_details

AwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesList: TypeAlias = list[
    "capo_securityhub.types.aws_ecs_task_definition_proxy_configuration_proxy_configuration_properties_details.AwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesDetails"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesList,
) -> list:
    import capo_securityhub.types.aws_ecs_task_definition_proxy_configuration_proxy_configuration_properties_details

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_ecs_task_definition_proxy_configuration_proxy_configuration_properties_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> AwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesList:
    import capo_securityhub.types.aws_ecs_task_definition_proxy_configuration_proxy_configuration_properties_details

    out: AwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesList = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_ecs_task_definition_proxy_configuration_proxy_configuration_properties_details.deserialize_json(
                item
            )
        )
    return out
