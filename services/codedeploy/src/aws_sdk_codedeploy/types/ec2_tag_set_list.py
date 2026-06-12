"""Generated from Smithy shape ``com.amazonaws.codedeploy#EC2TagSetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.ec2_tag_filter_list

EC2TagSetList: TypeAlias = list[
    "aws_sdk_codedeploy.types.ec2_tag_filter_list.EC2TagFilterList"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EC2TagSetList) -> list:
    import aws_sdk_codedeploy.types.ec2_tag_filter_list

    out: list = []
    for item in value:
        out.append(
            aws_sdk_codedeploy.types.ec2_tag_filter_list.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EC2TagSetList:
    import aws_sdk_codedeploy.types.ec2_tag_filter_list

    out: EC2TagSetList = []
    for item in data:
        out.append(
            aws_sdk_codedeploy.types.ec2_tag_filter_list.deserialize_aws_json_1_1(item)
        )
    return out
