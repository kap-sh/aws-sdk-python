"""Generated from Smithy shape ``com.amazonaws.networkfirewall#UpdateAvailabilityZoneChangeProtectionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.boolean
    import aws_sdk_network_firewall.types.resource_arn
    import aws_sdk_network_firewall.types.resource_name
    import aws_sdk_network_firewall.types.update_token


class UpdateAvailabilityZoneChangeProtectionRequest(TypedDict):
    update_token: NotRequired["aws_sdk_network_firewall.types.update_token.UpdateToken"]
    """<p>An optional token that you can use for optimistic locking. Network Firewall returns a token to your requests that access the firewall. The token marks the state of the firewall resource at the time of the request. </p> <p>To make an unconditional change to the firewall, omit the token in your update request. Without the token, Network Firewall performs your updates regardless of whether the firewall has changed since you last retrieved it.</p> <p>To make a conditional change to the firewall, provide the token in your update request. Network Firewall uses the token to ensure that the firewall hasn't changed since you last retrieved it. If it has changed, the operation fails with an <code>InvalidTokenException</code>. If this happens, retrieve the firewall again to get a current copy of it with a new token. Reapply your changes as needed, then try the operation again using the new token. </p>"""
    firewall_arn: NotRequired["aws_sdk_network_firewall.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the firewall.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""
    firewall_name: NotRequired[
        "aws_sdk_network_firewall.types.resource_name.ResourceName"
    ]
    """<p>The descriptive name of the firewall. You can't change the name of a firewall after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""
    availability_zone_change_protection: (
        "aws_sdk_network_firewall.types.boolean.Boolean"
    )
    """<p>A setting indicating whether the firewall is protected against changes to the subnet associations. Use this setting to protect against accidentally modifying the subnet associations for a firewall that is in use. When you create a firewall, the operation initializes this setting to <code>TRUE</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: UpdateAvailabilityZoneChangeProtectionRequest,
) -> dict:
    out: dict = {}
    if "update_token" in value:
        out["UpdateToken"] = value["update_token"]
    if "firewall_arn" in value:
        out["FirewallArn"] = value["firewall_arn"]
    if "firewall_name" in value:
        out["FirewallName"] = value["firewall_name"]
    out["AvailabilityZoneChangeProtection"] = value.get(
        "availability_zone_change_protection", False
    )
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> UpdateAvailabilityZoneChangeProtectionRequest:
    out: UpdateAvailabilityZoneChangeProtectionRequest = {}  # type: ignore[typeddict-item]
    if "UpdateToken" in data:
        out["update_token"] = data["UpdateToken"]
    if "FirewallArn" in data:
        out["firewall_arn"] = data["FirewallArn"]
    if "FirewallName" in data:
        out["firewall_name"] = data["FirewallName"]
    if "AvailabilityZoneChangeProtection" in data:
        out["availability_zone_change_protection"] = data[
            "AvailabilityZoneChangeProtection"
        ]
    else:
        out["availability_zone_change_protection"] = False
    return out
