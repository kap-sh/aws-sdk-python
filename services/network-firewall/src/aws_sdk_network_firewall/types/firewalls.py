"""Generated from Smithy shape ``com.amazonaws.networkfirewall#Firewalls``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.firewall_metadata

Firewalls: TypeAlias = list[
    "aws_sdk_network_firewall.types.firewall_metadata.FirewallMetadata"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Firewalls) -> list:
    import aws_sdk_network_firewall.types.firewall_metadata

    out: list = []
    for item in value:
        out.append(
            aws_sdk_network_firewall.types.firewall_metadata.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> Firewalls:
    import aws_sdk_network_firewall.types.firewall_metadata

    out: Firewalls = []
    for item in data:
        out.append(
            aws_sdk_network_firewall.types.firewall_metadata.deserialize_aws_json_1_0(
                item
            )
        )
    return out
