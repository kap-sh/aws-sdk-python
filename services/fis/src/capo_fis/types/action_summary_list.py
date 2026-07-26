"""Generated from Smithy shape ``com.amazonaws.fis#ActionSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fis.types.action_summary

ActionSummaryList: TypeAlias = list["capo_fis.types.action_summary.ActionSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: ActionSummaryList) -> list:
    import capo_fis.types.action_summary

    out: list = []
    for item in value:
        out.append(capo_fis.types.action_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ActionSummaryList:
    import capo_fis.types.action_summary

    out: ActionSummaryList = []
    for item in data:
        out.append(capo_fis.types.action_summary.deserialize_json(item))
    return out
