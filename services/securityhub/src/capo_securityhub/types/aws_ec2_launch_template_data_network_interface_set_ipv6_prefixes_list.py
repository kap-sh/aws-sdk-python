"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6PrefixesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_ec2_launch_template_data_network_interface_set_ipv6_prefixes_details

AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6PrefixesList: TypeAlias = list[
    "capo_securityhub.types.aws_ec2_launch_template_data_network_interface_set_ipv6_prefixes_details.AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6PrefixesDetails"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6PrefixesList,
) -> list:
    import capo_securityhub.types.aws_ec2_launch_template_data_network_interface_set_ipv6_prefixes_details

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_ec2_launch_template_data_network_interface_set_ipv6_prefixes_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6PrefixesList:
    import capo_securityhub.types.aws_ec2_launch_template_data_network_interface_set_ipv6_prefixes_details

    out: AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6PrefixesList = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_ec2_launch_template_data_network_interface_set_ipv6_prefixes_details.deserialize_json(
                item
            )
        )
    return out
