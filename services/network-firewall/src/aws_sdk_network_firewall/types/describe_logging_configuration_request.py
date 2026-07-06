"""Generated from Smithy shape ``com.amazonaws.networkfirewall#DescribeLoggingConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.resource_arn
    import aws_sdk_network_firewall.types.resource_name


class DescribeLoggingConfigurationRequest(TypedDict, closed=True):
    firewall_arn: NotRequired["aws_sdk_network_firewall.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the firewall.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""
    firewall_name: NotRequired[
        "aws_sdk_network_firewall.types.resource_name.ResourceName"
    ]
    """<p>The descriptive name of the firewall. You can't change the name of a firewall after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeLoggingConfigurationRequest) -> dict:
    out: dict = {}
    if "firewall_arn" in value:
        out["FirewallArn"] = value["firewall_arn"]
    if "firewall_name" in value:
        out["FirewallName"] = value["firewall_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeLoggingConfigurationRequest:
    out: DescribeLoggingConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "FirewallArn" in data:
        out["firewall_arn"] = data["FirewallArn"]
    if "FirewallName" in data:
        out["firewall_name"] = data["FirewallName"]
    return out
