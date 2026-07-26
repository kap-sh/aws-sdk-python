"""Generated from Smithy shape ``com.amazonaws.eks#AutoScalingGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_eks.types.auto_scaling_group

AutoScalingGroupList: TypeAlias = list[
    "capo_eks.types.auto_scaling_group.AutoScalingGroup"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutoScalingGroupList) -> list:
    import capo_eks.types.auto_scaling_group

    out: list = []
    for item in value:
        out.append(capo_eks.types.auto_scaling_group.serialize_json(item))
    return out


def deserialize_json(data: list) -> AutoScalingGroupList:
    import capo_eks.types.auto_scaling_group

    out: AutoScalingGroupList = []
    for item in data:
        out.append(capo_eks.types.auto_scaling_group.deserialize_json(item))
    return out
