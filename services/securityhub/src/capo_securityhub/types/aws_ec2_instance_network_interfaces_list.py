"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2InstanceNetworkInterfacesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_ec2_instance_network_interfaces_details

AwsEc2InstanceNetworkInterfacesList: TypeAlias = list[
    "capo_securityhub.types.aws_ec2_instance_network_interfaces_details.AwsEc2InstanceNetworkInterfacesDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2InstanceNetworkInterfacesList) -> list:
    import capo_securityhub.types.aws_ec2_instance_network_interfaces_details

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_ec2_instance_network_interfaces_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsEc2InstanceNetworkInterfacesList:
    import capo_securityhub.types.aws_ec2_instance_network_interfaces_details

    out: AwsEc2InstanceNetworkInterfacesList = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_ec2_instance_network_interfaces_details.deserialize_json(
                item
            )
        )
    return out
