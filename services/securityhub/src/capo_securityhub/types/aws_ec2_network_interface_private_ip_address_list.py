"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2NetworkInterfacePrivateIpAddressList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_ec2_network_interface_private_ip_address_detail

AwsEc2NetworkInterfacePrivateIpAddressList: TypeAlias = list[
    "capo_securityhub.types.aws_ec2_network_interface_private_ip_address_detail.AwsEc2NetworkInterfacePrivateIpAddressDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2NetworkInterfacePrivateIpAddressList) -> list:
    import capo_securityhub.types.aws_ec2_network_interface_private_ip_address_detail

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_ec2_network_interface_private_ip_address_detail.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsEc2NetworkInterfacePrivateIpAddressList:
    import capo_securityhub.types.aws_ec2_network_interface_private_ip_address_detail

    out: AwsEc2NetworkInterfacePrivateIpAddressList = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_ec2_network_interface_private_ip_address_detail.deserialize_json(
                item
            )
        )
    return out
