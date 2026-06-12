"""Generated from Smithy shape ``com.amazonaws.vpclattice#TargetSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.target_summary

TargetSummaryList: TypeAlias = list[
    "aws_sdk_vpc_lattice.types.target_summary.TargetSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: TargetSummaryList) -> list:
    import aws_sdk_vpc_lattice.types.target_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_vpc_lattice.types.target_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> TargetSummaryList:
    import aws_sdk_vpc_lattice.types.target_summary

    out: TargetSummaryList = []
    for item in data:
        out.append(aws_sdk_vpc_lattice.types.target_summary.deserialize_json(item))
    return out
