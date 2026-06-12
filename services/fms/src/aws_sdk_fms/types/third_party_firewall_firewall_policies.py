"""Generated from Smithy shape ``com.amazonaws.fms#ThirdPartyFirewallFirewallPolicies``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fms.types.third_party_firewall_firewall_policy

ThirdPartyFirewallFirewallPolicies: TypeAlias = list[
    "aws_sdk_fms.types.third_party_firewall_firewall_policy.ThirdPartyFirewallFirewallPolicy"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ThirdPartyFirewallFirewallPolicies) -> list:
    import aws_sdk_fms.types.third_party_firewall_firewall_policy

    out: list = []
    for item in value:
        out.append(
            aws_sdk_fms.types.third_party_firewall_firewall_policy.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ThirdPartyFirewallFirewallPolicies:
    import aws_sdk_fms.types.third_party_firewall_firewall_policy

    out: ThirdPartyFirewallFirewallPolicies = []
    for item in data:
        out.append(
            aws_sdk_fms.types.third_party_firewall_firewall_policy.deserialize_aws_json_1_1(
                item
            )
        )
    return out
