"""Generated from Smithy shape ``com.amazonaws.networkfirewall#FirewallPolicies``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.firewall_policy_metadata

FirewallPolicies: TypeAlias = list[
    "aws_sdk_network_firewall.types.firewall_policy_metadata.FirewallPolicyMetadata"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FirewallPolicies) -> list:
    import aws_sdk_network_firewall.types.firewall_policy_metadata

    out: list = []
    for item in value:
        out.append(
            aws_sdk_network_firewall.types.firewall_policy_metadata.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> FirewallPolicies:
    import aws_sdk_network_firewall.types.firewall_policy_metadata

    out: FirewallPolicies = []
    for item in data:
        out.append(
            aws_sdk_network_firewall.types.firewall_policy_metadata.deserialize_aws_json_1_0(
                item
            )
        )
    return out
