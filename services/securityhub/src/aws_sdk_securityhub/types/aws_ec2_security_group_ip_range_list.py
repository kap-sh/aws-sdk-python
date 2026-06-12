"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2SecurityGroupIpRangeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_ec2_security_group_ip_range

AwsEc2SecurityGroupIpRangeList: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_ec2_security_group_ip_range.AwsEc2SecurityGroupIpRange"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2SecurityGroupIpRangeList) -> list:
    import aws_sdk_securityhub.types.aws_ec2_security_group_ip_range

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_ec2_security_group_ip_range.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsEc2SecurityGroupIpRangeList:
    import aws_sdk_securityhub.types.aws_ec2_security_group_ip_range

    out: AwsEc2SecurityGroupIpRangeList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_ec2_security_group_ip_range.deserialize_json(
                item
            )
        )
    return out
