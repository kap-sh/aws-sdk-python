"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2InstanceNetworkInterfacesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_ec2_instance_network_interfaces_details

AwsEc2InstanceNetworkInterfacesList: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_ec2_instance_network_interfaces_details.AwsEc2InstanceNetworkInterfacesDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2InstanceNetworkInterfacesList) -> list:
    import aws_sdk_securityhub.types.aws_ec2_instance_network_interfaces_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_ec2_instance_network_interfaces_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsEc2InstanceNetworkInterfacesList:
    import aws_sdk_securityhub.types.aws_ec2_instance_network_interfaces_details

    out: AwsEc2InstanceNetworkInterfacesList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_ec2_instance_network_interfaces_details.deserialize_json(
                item
            )
        )
    return out
