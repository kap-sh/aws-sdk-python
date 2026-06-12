"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsNetworkFirewallFirewallSubnetMappingsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_network_firewall_firewall_subnet_mappings_details

AwsNetworkFirewallFirewallSubnetMappingsList: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_network_firewall_firewall_subnet_mappings_details.AwsNetworkFirewallFirewallSubnetMappingsDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsNetworkFirewallFirewallSubnetMappingsList) -> list:
    import aws_sdk_securityhub.types.aws_network_firewall_firewall_subnet_mappings_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_network_firewall_firewall_subnet_mappings_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsNetworkFirewallFirewallSubnetMappingsList:
    import aws_sdk_securityhub.types.aws_network_firewall_firewall_subnet_mappings_details

    out: AwsNetworkFirewallFirewallSubnetMappingsList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_network_firewall_firewall_subnet_mappings_details.deserialize_json(
                item
            )
        )
    return out
