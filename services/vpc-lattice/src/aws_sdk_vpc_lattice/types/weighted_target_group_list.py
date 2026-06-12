"""Generated from Smithy shape ``com.amazonaws.vpclattice#WeightedTargetGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.weighted_target_group

WeightedTargetGroupList: TypeAlias = list[
    "aws_sdk_vpc_lattice.types.weighted_target_group.WeightedTargetGroup"
]


# --- restJson1 ser/de ---
def serialize_json(value: WeightedTargetGroupList) -> list:
    import aws_sdk_vpc_lattice.types.weighted_target_group

    out: list = []
    for item in value:
        out.append(aws_sdk_vpc_lattice.types.weighted_target_group.serialize_json(item))
    return out


def deserialize_json(data: list) -> WeightedTargetGroupList:
    import aws_sdk_vpc_lattice.types.weighted_target_group

    out: WeightedTargetGroupList = []
    for item in data:
        out.append(
            aws_sdk_vpc_lattice.types.weighted_target_group.deserialize_json(item)
        )
    return out
