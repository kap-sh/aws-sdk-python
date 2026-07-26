"""Generated from Smithy shape ``com.amazonaws.qbusiness#GroupSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qbusiness.types.group_summary

GroupSummaryList: TypeAlias = list["capo_qbusiness.types.group_summary.GroupSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: GroupSummaryList) -> list:
    import capo_qbusiness.types.group_summary

    out: list = []
    for item in value:
        out.append(capo_qbusiness.types.group_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> GroupSummaryList:
    import capo_qbusiness.types.group_summary

    out: GroupSummaryList = []
    for item in data:
        out.append(capo_qbusiness.types.group_summary.deserialize_json(item))
    return out
