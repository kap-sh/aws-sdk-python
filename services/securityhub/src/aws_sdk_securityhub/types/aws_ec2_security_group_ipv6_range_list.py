"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2SecurityGroupIpv6RangeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_ec2_security_group_ipv6_range

AwsEc2SecurityGroupIpv6RangeList: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_ec2_security_group_ipv6_range.AwsEc2SecurityGroupIpv6Range"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2SecurityGroupIpv6RangeList) -> list:
    import aws_sdk_securityhub.types.aws_ec2_security_group_ipv6_range

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_ec2_security_group_ipv6_range.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsEc2SecurityGroupIpv6RangeList:
    import aws_sdk_securityhub.types.aws_ec2_security_group_ipv6_range

    out: AwsEc2SecurityGroupIpv6RangeList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_ec2_security_group_ipv6_range.deserialize_json(
                item
            )
        )
    return out
