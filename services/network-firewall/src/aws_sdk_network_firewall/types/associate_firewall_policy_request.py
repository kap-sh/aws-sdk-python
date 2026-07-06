"""Generated from Smithy shape ``com.amazonaws.networkfirewall#AssociateFirewallPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_network_firewall.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.resource_arn
    import aws_sdk_network_firewall.types.resource_name
    import aws_sdk_network_firewall.types.update_token


class AssociateFirewallPolicyRequest(TypedDict, closed=True):
    update_token: NotRequired["aws_sdk_network_firewall.types.update_token.UpdateToken"]
    """<p>An optional token that you can use for optimistic locking. Network Firewall returns a token to your requests that access the firewall. The token marks the state of the firewall resource at the time of the request. </p> <p>To make an unconditional change to the firewall, omit the token in your update request. Without the token, Network Firewall performs your updates regardless of whether the firewall has changed since you last retrieved it.</p> <p>To make a conditional change to the firewall, provide the token in your update request. Network Firewall uses the token to ensure that the firewall hasn't changed since you last retrieved it. If it has changed, the operation fails with an <code>InvalidTokenException</code>. If this happens, retrieve the firewall again to get a current copy of it with a new token. Reapply your changes as needed, then try the operation again using the new token. </p>"""
    firewall_arn: NotRequired["aws_sdk_network_firewall.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the firewall.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""
    firewall_name: NotRequired[
        "aws_sdk_network_firewall.types.resource_name.ResourceName"
    ]
    """<p>The descriptive name of the firewall. You can't change the name of a firewall after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""
    firewall_policy_arn: "aws_sdk_network_firewall.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the firewall policy.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AssociateFirewallPolicyRequest) -> dict:
    out: dict = {}
    if "update_token" in value:
        out["UpdateToken"] = value["update_token"]
    if "firewall_arn" in value:
        out["FirewallArn"] = value["firewall_arn"]
    if "firewall_name" in value:
        out["FirewallName"] = value["firewall_name"]
    out["FirewallPolicyArn"] = value["firewall_policy_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AssociateFirewallPolicyRequest:
    out: AssociateFirewallPolicyRequest = {}  # type: ignore[typeddict-item]
    if "UpdateToken" in data:
        out["update_token"] = data["UpdateToken"]
    if "FirewallArn" in data:
        out["firewall_arn"] = data["FirewallArn"]
    if "FirewallName" in data:
        out["firewall_name"] = data["FirewallName"]
    if "FirewallPolicyArn" in data:
        out["firewall_policy_arn"] = data["FirewallPolicyArn"]
    else:
        raise DeserializationError(
            "AssociateFirewallPolicyRequest.firewall_policy_arn required"
        )
    return out
