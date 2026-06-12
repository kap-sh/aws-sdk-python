"""Generated from Smithy shape ``com.amazonaws.codedeploy#EC2TagFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.ec2_tag_filter

EC2TagFilterList: TypeAlias = list[
    "aws_sdk_codedeploy.types.ec2_tag_filter.EC2TagFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EC2TagFilterList) -> list:
    import aws_sdk_codedeploy.types.ec2_tag_filter

    out: list = []
    for item in value:
        out.append(aws_sdk_codedeploy.types.ec2_tag_filter.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> EC2TagFilterList:
    import aws_sdk_codedeploy.types.ec2_tag_filter

    out: EC2TagFilterList = []
    for item in data:
        out.append(
            aws_sdk_codedeploy.types.ec2_tag_filter.deserialize_aws_json_1_1(item)
        )
    return out
