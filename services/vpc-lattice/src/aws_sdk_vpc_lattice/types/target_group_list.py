"""Generated from Smithy shape ``com.amazonaws.vpclattice#TargetGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.target_group_summary

TargetGroupList: TypeAlias = list[
    "aws_sdk_vpc_lattice.types.target_group_summary.TargetGroupSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: TargetGroupList) -> list:
    import aws_sdk_vpc_lattice.types.target_group_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_vpc_lattice.types.target_group_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> TargetGroupList:
    import aws_sdk_vpc_lattice.types.target_group_summary

    out: TargetGroupList = []
    for item in data:
        out.append(
            aws_sdk_vpc_lattice.types.target_group_summary.deserialize_json(item)
        )
    return out
