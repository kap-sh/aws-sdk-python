"""Generated from Smithy shape ``com.amazonaws.synthetics#GroupSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_synthetics.types.group_summary

GroupSummaryList: TypeAlias = list["capo_synthetics.types.group_summary.GroupSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: GroupSummaryList) -> list:
    import capo_synthetics.types.group_summary

    out: list = []
    for item in value:
        out.append(capo_synthetics.types.group_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> GroupSummaryList:
    import capo_synthetics.types.group_summary

    out: GroupSummaryList = []
    for item in data:
        out.append(capo_synthetics.types.group_summary.deserialize_json(item))
    return out
