"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv4PrefixesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_ec2_launch_template_data_network_interface_set_ipv4_prefixes_details

AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv4PrefixesList: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_ec2_launch_template_data_network_interface_set_ipv4_prefixes_details.AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv4PrefixesDetails"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv4PrefixesList,
) -> list:
    import aws_sdk_securityhub.types.aws_ec2_launch_template_data_network_interface_set_ipv4_prefixes_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_ec2_launch_template_data_network_interface_set_ipv4_prefixes_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv4PrefixesList:
    import aws_sdk_securityhub.types.aws_ec2_launch_template_data_network_interface_set_ipv4_prefixes_details

    out: AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv4PrefixesList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_ec2_launch_template_data_network_interface_set_ipv4_prefixes_details.deserialize_json(
                item
            )
        )
    return out
