"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2NetworkInterfaceSecurityGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_ec2_network_interface_security_group

AwsEc2NetworkInterfaceSecurityGroupList: TypeAlias = list[
    "capo_securityhub.types.aws_ec2_network_interface_security_group.AwsEc2NetworkInterfaceSecurityGroup"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2NetworkInterfaceSecurityGroupList) -> list:
    import capo_securityhub.types.aws_ec2_network_interface_security_group

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_ec2_network_interface_security_group.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsEc2NetworkInterfaceSecurityGroupList:
    import capo_securityhub.types.aws_ec2_network_interface_security_group

    out: AwsEc2NetworkInterfaceSecurityGroupList = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_ec2_network_interface_security_group.deserialize_json(
                item
            )
        )
    return out
