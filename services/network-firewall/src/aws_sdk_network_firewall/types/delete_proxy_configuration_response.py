"""Generated from Smithy shape ``com.amazonaws.networkfirewall#DeleteProxyConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.resource_arn
    import aws_sdk_network_firewall.types.resource_name


class DeleteProxyConfigurationResponse(TypedDict):
    proxy_configuration_name: NotRequired[
        "aws_sdk_network_firewall.types.resource_name.ResourceName"
    ]
    """<p>The descriptive name of the proxy configuration. You can't change the name of a proxy configuration after you create it.</p>"""
    proxy_configuration_arn: NotRequired[
        "aws_sdk_network_firewall.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of a proxy configuration.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteProxyConfigurationResponse) -> dict:
    out: dict = {}
    if "proxy_configuration_name" in value:
        out["ProxyConfigurationName"] = value["proxy_configuration_name"]
    if "proxy_configuration_arn" in value:
        out["ProxyConfigurationArn"] = value["proxy_configuration_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteProxyConfigurationResponse:
    out: DeleteProxyConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "ProxyConfigurationName" in data:
        out["proxy_configuration_name"] = data["ProxyConfigurationName"]
    if "ProxyConfigurationArn" in data:
        out["proxy_configuration_arn"] = data["ProxyConfigurationArn"]
    return out
