"""Generated from Smithy shape ``com.amazonaws.connect#HierarchyGroupSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.hierarchy_group_summary

HierarchyGroupSummaryList: TypeAlias = list[
    "aws_sdk_connect.types.hierarchy_group_summary.HierarchyGroupSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: HierarchyGroupSummaryList) -> list:
    import aws_sdk_connect.types.hierarchy_group_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.hierarchy_group_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> HierarchyGroupSummaryList:
    import aws_sdk_connect.types.hierarchy_group_summary

    out: HierarchyGroupSummaryList = []
    for item in data:
        out.append(aws_sdk_connect.types.hierarchy_group_summary.deserialize_json(item))
    return out
