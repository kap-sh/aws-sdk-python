"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsNetworkFirewallFirewallPolicyDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.firewall_policy_details
    import aws_sdk_securityhub.types.non_empty_string


class AwsNetworkFirewallFirewallPolicyDetails(TypedDict):
    firewall_policy: NotRequired[
        "aws_sdk_securityhub.types.firewall_policy_details.FirewallPolicyDetails"
    ]
    """<p>The firewall policy configuration.</p>"""
    firewall_policy_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ARN of the firewall policy.</p>"""
    firewall_policy_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The identifier of the firewall policy.</p>"""
    firewall_policy_name: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the firewall policy.</p>"""
    description: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>A description of the firewall policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsNetworkFirewallFirewallPolicyDetails) -> dict:
    out: dict = {}
    if "firewall_policy" in value:
        import aws_sdk_securityhub.types.firewall_policy_details

        out["FirewallPolicy"] = (
            aws_sdk_securityhub.types.firewall_policy_details.serialize_json(
                value["firewall_policy"]
            )
        )
    if "firewall_policy_arn" in value:
        out["FirewallPolicyArn"] = value["firewall_policy_arn"]
    if "firewall_policy_id" in value:
        out["FirewallPolicyId"] = value["firewall_policy_id"]
    if "firewall_policy_name" in value:
        out["FirewallPolicyName"] = value["firewall_policy_name"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_json(data: dict) -> AwsNetworkFirewallFirewallPolicyDetails:
    out: AwsNetworkFirewallFirewallPolicyDetails = {}  # type: ignore[typeddict-item]
    if "FirewallPolicy" in data:
        import aws_sdk_securityhub.types.firewall_policy_details

        out["firewall_policy"] = (
            aws_sdk_securityhub.types.firewall_policy_details.deserialize_json(
                data["FirewallPolicy"]
            )
        )
    if "FirewallPolicyArn" in data:
        out["firewall_policy_arn"] = data["FirewallPolicyArn"]
    if "FirewallPolicyId" in data:
        out["firewall_policy_id"] = data["FirewallPolicyId"]
    if "FirewallPolicyName" in data:
        out["firewall_policy_name"] = data["FirewallPolicyName"]
    if "Description" in data:
        out["description"] = data["Description"]
    return out
