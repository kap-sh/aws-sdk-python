"""Generated from Smithy shape ``com.amazonaws.networkfirewall#DeleteFirewallRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.resource_arn
    import aws_sdk_network_firewall.types.resource_name


class DeleteFirewallRequest(TypedDict):
    firewall_name: NotRequired[
        "aws_sdk_network_firewall.types.resource_name.ResourceName"
    ]
    """<p>The descriptive name of the firewall. You can't change the name of a firewall after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""
    firewall_arn: NotRequired["aws_sdk_network_firewall.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the firewall.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteFirewallRequest) -> dict:
    out: dict = {}
    if "firewall_name" in value:
        out["FirewallName"] = value["firewall_name"]
    if "firewall_arn" in value:
        out["FirewallArn"] = value["firewall_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteFirewallRequest:
    out: DeleteFirewallRequest = {}  # type: ignore[typeddict-item]
    if "FirewallName" in data:
        out["firewall_name"] = data["FirewallName"]
    if "FirewallArn" in data:
        out["firewall_arn"] = data["FirewallArn"]
    return out
