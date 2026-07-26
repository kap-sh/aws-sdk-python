"""Generated from Smithy shape ``com.amazonaws.rtbfabric#AutoScalingGroupNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rtbfabric.types.auto_scaling_group_name

AutoScalingGroupNameList: TypeAlias = list[
    "capo_rtbfabric.types.auto_scaling_group_name.AutoScalingGroupName"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutoScalingGroupNameList) -> list:
    return list(value)


def deserialize_json(data: list) -> AutoScalingGroupNameList:
    return list(data)
