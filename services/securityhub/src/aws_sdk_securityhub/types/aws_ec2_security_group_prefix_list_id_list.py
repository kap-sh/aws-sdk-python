"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2SecurityGroupPrefixListIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_ec2_security_group_prefix_list_id

AwsEc2SecurityGroupPrefixListIdList: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_ec2_security_group_prefix_list_id.AwsEc2SecurityGroupPrefixListId"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2SecurityGroupPrefixListIdList) -> list:
    import aws_sdk_securityhub.types.aws_ec2_security_group_prefix_list_id

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_ec2_security_group_prefix_list_id.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsEc2SecurityGroupPrefixListIdList:
    import aws_sdk_securityhub.types.aws_ec2_security_group_prefix_list_id

    out: AwsEc2SecurityGroupPrefixListIdList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_ec2_security_group_prefix_list_id.deserialize_json(
                item
            )
        )
    return out
