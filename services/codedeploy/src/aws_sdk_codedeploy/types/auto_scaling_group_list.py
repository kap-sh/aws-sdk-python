"""Generated from Smithy shape ``com.amazonaws.codedeploy#AutoScalingGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.auto_scaling_group

AutoScalingGroupList: TypeAlias = list[
    "aws_sdk_codedeploy.types.auto_scaling_group.AutoScalingGroup"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoScalingGroupList) -> list:
    import aws_sdk_codedeploy.types.auto_scaling_group

    out: list = []
    for item in value:
        out.append(
            aws_sdk_codedeploy.types.auto_scaling_group.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AutoScalingGroupList:
    import aws_sdk_codedeploy.types.auto_scaling_group

    out: AutoScalingGroupList = []
    for item in data:
        out.append(
            aws_sdk_codedeploy.types.auto_scaling_group.deserialize_aws_json_1_1(item)
        )
    return out
