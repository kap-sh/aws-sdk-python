"""Generated from Smithy shape ``com.amazonaws.connect#HierarchyGroupSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.hierarchy_group_summary

HierarchyGroupSummaryList: TypeAlias = list[
    "capo_connect.types.hierarchy_group_summary.HierarchyGroupSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: HierarchyGroupSummaryList) -> list:
    import capo_connect.types.hierarchy_group_summary

    out: list = []
    for item in value:
        out.append(capo_connect.types.hierarchy_group_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> HierarchyGroupSummaryList:
    import capo_connect.types.hierarchy_group_summary

    out: HierarchyGroupSummaryList = []
    for item in data:
        out.append(capo_connect.types.hierarchy_group_summary.deserialize_json(item))
    return out
