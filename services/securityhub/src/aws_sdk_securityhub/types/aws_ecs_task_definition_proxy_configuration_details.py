"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsTaskDefinitionProxyConfigurationDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_ecs_task_definition_proxy_configuration_proxy_configuration_properties_list
    import aws_sdk_securityhub.types.non_empty_string


class AwsEcsTaskDefinitionProxyConfigurationDetails(TypedDict):
    container_name: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the container that will serve as the App Mesh proxy.</p>"""
    proxy_configuration_properties: NotRequired[
        "aws_sdk_securityhub.types.aws_ecs_task_definition_proxy_configuration_proxy_configuration_properties_list.AwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesList"
    ]
    """<p>The set of network configuration parameters to provide to the Container Network Interface (CNI) plugin, specified as key-value pairs.</p>"""
    type: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The proxy type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEcsTaskDefinitionProxyConfigurationDetails) -> dict:
    out: dict = {}
    if "container_name" in value:
        out["ContainerName"] = value["container_name"]
    if "proxy_configuration_properties" in value:
        import aws_sdk_securityhub.types.aws_ecs_task_definition_proxy_configuration_proxy_configuration_properties_list

        out["ProxyConfigurationProperties"] = (
            aws_sdk_securityhub.types.aws_ecs_task_definition_proxy_configuration_proxy_configuration_properties_list.serialize_json(
                value["proxy_configuration_properties"]
            )
        )
    if "type" in value:
        out["Type"] = value["type"]
    return out


def deserialize_json(data: dict) -> AwsEcsTaskDefinitionProxyConfigurationDetails:
    out: AwsEcsTaskDefinitionProxyConfigurationDetails = {}  # type: ignore[typeddict-item]
    if "ContainerName" in data:
        out["container_name"] = data["ContainerName"]
    if "ProxyConfigurationProperties" in data:
        import aws_sdk_securityhub.types.aws_ecs_task_definition_proxy_configuration_proxy_configuration_properties_list

        out["proxy_configuration_properties"] = (
            aws_sdk_securityhub.types.aws_ecs_task_definition_proxy_configuration_proxy_configuration_properties_list.deserialize_json(
                data["ProxyConfigurationProperties"]
            )
        )
    if "Type" in data:
        out["type"] = data["Type"]
    return out
