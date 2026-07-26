"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6AddressesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_ec2_launch_template_data_network_interface_set_ipv6_addresses_details

AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6AddressesList: TypeAlias = list[
    "capo_securityhub.types.aws_ec2_launch_template_data_network_interface_set_ipv6_addresses_details.AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6AddressesDetails"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6AddressesList,
) -> list:
    import capo_securityhub.types.aws_ec2_launch_template_data_network_interface_set_ipv6_addresses_details

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_ec2_launch_template_data_network_interface_set_ipv6_addresses_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6AddressesList:
    import capo_securityhub.types.aws_ec2_launch_template_data_network_interface_set_ipv6_addresses_details

    out: AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6AddressesList = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_ec2_launch_template_data_network_interface_set_ipv6_addresses_details.deserialize_json(
                item
            )
        )
    return out
