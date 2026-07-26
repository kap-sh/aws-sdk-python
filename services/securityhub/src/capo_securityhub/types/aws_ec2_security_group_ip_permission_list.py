"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2SecurityGroupIpPermissionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_ec2_security_group_ip_permission

AwsEc2SecurityGroupIpPermissionList: TypeAlias = list[
    "capo_securityhub.types.aws_ec2_security_group_ip_permission.AwsEc2SecurityGroupIpPermission"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2SecurityGroupIpPermissionList) -> list:
    import capo_securityhub.types.aws_ec2_security_group_ip_permission

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_ec2_security_group_ip_permission.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsEc2SecurityGroupIpPermissionList:
    import capo_securityhub.types.aws_ec2_security_group_ip_permission

    out: AwsEc2SecurityGroupIpPermissionList = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_ec2_security_group_ip_permission.deserialize_json(
                item
            )
        )
    return out
