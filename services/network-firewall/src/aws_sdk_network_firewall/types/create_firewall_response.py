"""Generated from Smithy shape ``com.amazonaws.networkfirewall#CreateFirewallResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.firewall
    import aws_sdk_network_firewall.types.firewall_status


class CreateFirewallResponse(TypedDict):
    firewall: NotRequired["aws_sdk_network_firewall.types.firewall.Firewall"]
    """<p>The configuration settings for the firewall. These settings include the firewall policy and the subnets in your VPC to use for the firewall endpoints. </p>"""
    firewall_status: NotRequired[
        "aws_sdk_network_firewall.types.firewall_status.FirewallStatus"
    ]
    """<p>Detailed information about the current status of a <a>Firewall</a>. You can retrieve this for a firewall by calling <a>DescribeFirewall</a> and providing the firewall name and ARN.</p> <p>The firewall status indicates a combined status. It indicates whether all subnets are up-to-date with the latest firewall configurations, which is based on the sync states config values, and also whether all subnets have their endpoints fully enabled, based on their sync states attachment values. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateFirewallResponse) -> dict:
    out: dict = {}
    if "firewall" in value:
        import aws_sdk_network_firewall.types.firewall

        out["Firewall"] = (
            aws_sdk_network_firewall.types.firewall.serialize_aws_json_1_0(
                value["firewall"]
            )
        )
    if "firewall_status" in value:
        import aws_sdk_network_firewall.types.firewall_status

        out["FirewallStatus"] = (
            aws_sdk_network_firewall.types.firewall_status.serialize_aws_json_1_0(
                value["firewall_status"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateFirewallResponse:
    out: CreateFirewallResponse = {}  # type: ignore[typeddict-item]
    if "Firewall" in data:
        import aws_sdk_network_firewall.types.firewall

        out["firewall"] = (
            aws_sdk_network_firewall.types.firewall.deserialize_aws_json_1_0(
                data["Firewall"]
            )
        )
    if "FirewallStatus" in data:
        import aws_sdk_network_firewall.types.firewall_status

        out["firewall_status"] = (
            aws_sdk_network_firewall.types.firewall_status.deserialize_aws_json_1_0(
                data["FirewallStatus"]
            )
        )
    return out
