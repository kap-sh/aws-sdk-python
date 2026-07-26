"""Generated from Smithy shape ``com.amazonaws.inspector#AutoScalingGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector.types.auto_scaling_group

AutoScalingGroupList: TypeAlias = list[
    "capo_inspector.types.auto_scaling_group.AutoScalingGroup"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoScalingGroupList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> AutoScalingGroupList:
    return list(data)
