"""Generated from Smithy shape ``com.amazonaws.fms#ThirdPartyFirewallFirewallPolicies``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fms.types.third_party_firewall_firewall_policy

ThirdPartyFirewallFirewallPolicies: TypeAlias = list[
    "capo_fms.types.third_party_firewall_firewall_policy.ThirdPartyFirewallFirewallPolicy"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ThirdPartyFirewallFirewallPolicies) -> list:
    import capo_fms.types.third_party_firewall_firewall_policy

    out: list = []
    for item in value:
        out.append(
            capo_fms.types.third_party_firewall_firewall_policy.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ThirdPartyFirewallFirewallPolicies:
    import capo_fms.types.third_party_firewall_firewall_policy

    out: ThirdPartyFirewallFirewallPolicies = []
    for item in data:
        out.append(
            capo_fms.types.third_party_firewall_firewall_policy.deserialize_aws_json_1_1(
                item
            )
        )
    return out
