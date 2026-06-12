"""Generated from Smithy shape ``com.amazonaws.finspace#KxScalingGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_finspace.types.kx_scaling_group

KxScalingGroupList: TypeAlias = list[
    "aws_sdk_finspace.types.kx_scaling_group.KxScalingGroup"
]


# --- restJson1 ser/de ---
def serialize_json(value: KxScalingGroupList) -> list:
    import aws_sdk_finspace.types.kx_scaling_group

    out: list = []
    for item in value:
        out.append(aws_sdk_finspace.types.kx_scaling_group.serialize_json(item))
    return out


def deserialize_json(data: list) -> KxScalingGroupList:
    import aws_sdk_finspace.types.kx_scaling_group

    out: KxScalingGroupList = []
    for item in data:
        out.append(aws_sdk_finspace.types.kx_scaling_group.deserialize_json(item))
    return out
