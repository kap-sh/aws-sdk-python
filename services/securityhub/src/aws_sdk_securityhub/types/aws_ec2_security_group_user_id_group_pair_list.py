"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2SecurityGroupUserIdGroupPairList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_ec2_security_group_user_id_group_pair

AwsEc2SecurityGroupUserIdGroupPairList: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_ec2_security_group_user_id_group_pair.AwsEc2SecurityGroupUserIdGroupPair"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2SecurityGroupUserIdGroupPairList) -> list:
    import aws_sdk_securityhub.types.aws_ec2_security_group_user_id_group_pair

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_ec2_security_group_user_id_group_pair.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsEc2SecurityGroupUserIdGroupPairList:
    import aws_sdk_securityhub.types.aws_ec2_security_group_user_id_group_pair

    out: AwsEc2SecurityGroupUserIdGroupPairList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_ec2_security_group_user_id_group_pair.deserialize_json(
                item
            )
        )
    return out
