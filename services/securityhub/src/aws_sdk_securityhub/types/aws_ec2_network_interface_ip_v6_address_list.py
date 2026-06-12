"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2NetworkInterfaceIpV6AddressList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_ec2_network_interface_ip_v6_address_detail

AwsEc2NetworkInterfaceIpV6AddressList: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_ec2_network_interface_ip_v6_address_detail.AwsEc2NetworkInterfaceIpV6AddressDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2NetworkInterfaceIpV6AddressList) -> list:
    import aws_sdk_securityhub.types.aws_ec2_network_interface_ip_v6_address_detail

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_ec2_network_interface_ip_v6_address_detail.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsEc2NetworkInterfaceIpV6AddressList:
    import aws_sdk_securityhub.types.aws_ec2_network_interface_ip_v6_address_detail

    out: AwsEc2NetworkInterfaceIpV6AddressList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_ec2_network_interface_ip_v6_address_detail.deserialize_json(
                item
            )
        )
    return out
