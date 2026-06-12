"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2LaunchTemplateDataNetworkInterfaceSetPrivateIpAddressesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_ec2_launch_template_data_network_interface_set_private_ip_addresses_details

AwsEc2LaunchTemplateDataNetworkInterfaceSetPrivateIpAddressesList: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_ec2_launch_template_data_network_interface_set_private_ip_addresses_details.AwsEc2LaunchTemplateDataNetworkInterfaceSetPrivateIpAddressesDetails"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEc2LaunchTemplateDataNetworkInterfaceSetPrivateIpAddressesList,
) -> list:
    import aws_sdk_securityhub.types.aws_ec2_launch_template_data_network_interface_set_private_ip_addresses_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_ec2_launch_template_data_network_interface_set_private_ip_addresses_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> AwsEc2LaunchTemplateDataNetworkInterfaceSetPrivateIpAddressesList:
    import aws_sdk_securityhub.types.aws_ec2_launch_template_data_network_interface_set_private_ip_addresses_details

    out: AwsEc2LaunchTemplateDataNetworkInterfaceSetPrivateIpAddressesList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_ec2_launch_template_data_network_interface_set_private_ip_addresses_details.deserialize_json(
                item
            )
        )
    return out
