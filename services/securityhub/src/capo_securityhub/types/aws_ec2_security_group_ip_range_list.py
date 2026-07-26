"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2SecurityGroupIpRangeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_ec2_security_group_ip_range

AwsEc2SecurityGroupIpRangeList: TypeAlias = list[
    "capo_securityhub.types.aws_ec2_security_group_ip_range.AwsEc2SecurityGroupIpRange"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2SecurityGroupIpRangeList) -> list:
    import capo_securityhub.types.aws_ec2_security_group_ip_range

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_ec2_security_group_ip_range.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AwsEc2SecurityGroupIpRangeList:
    import capo_securityhub.types.aws_ec2_security_group_ip_range

    out: AwsEc2SecurityGroupIpRangeList = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_ec2_security_group_ip_range.deserialize_json(
                item
            )
        )
    return out
