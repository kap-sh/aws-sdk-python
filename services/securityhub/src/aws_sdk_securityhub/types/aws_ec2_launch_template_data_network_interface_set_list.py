"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2LaunchTemplateDataNetworkInterfaceSetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_ec2_launch_template_data_network_interface_set_details

AwsEc2LaunchTemplateDataNetworkInterfaceSetList: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_ec2_launch_template_data_network_interface_set_details.AwsEc2LaunchTemplateDataNetworkInterfaceSetDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2LaunchTemplateDataNetworkInterfaceSetList) -> list:
    import aws_sdk_securityhub.types.aws_ec2_launch_template_data_network_interface_set_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_ec2_launch_template_data_network_interface_set_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsEc2LaunchTemplateDataNetworkInterfaceSetList:
    import aws_sdk_securityhub.types.aws_ec2_launch_template_data_network_interface_set_details

    out: AwsEc2LaunchTemplateDataNetworkInterfaceSetList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_ec2_launch_template_data_network_interface_set_details.deserialize_json(
                item
            )
        )
    return out
