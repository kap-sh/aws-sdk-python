"""Generated from Smithy shape ``com.amazonaws.codedeploy#AutoScalingGroupNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codedeploy.types.auto_scaling_group_name

AutoScalingGroupNameList: TypeAlias = list[
    "capo_codedeploy.types.auto_scaling_group_name.AutoScalingGroupName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoScalingGroupNameList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> AutoScalingGroupNameList:
    return list(data)
