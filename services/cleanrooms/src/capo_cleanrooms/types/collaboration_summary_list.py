"""Generated from Smithy shape ``com.amazonaws.cleanrooms#CollaborationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanrooms.types.collaboration_summary

CollaborationSummaryList: TypeAlias = list[
    "capo_cleanrooms.types.collaboration_summary.CollaborationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: CollaborationSummaryList) -> list:
    import capo_cleanrooms.types.collaboration_summary

    out: list = []
    for item in value:
        out.append(capo_cleanrooms.types.collaboration_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> CollaborationSummaryList:
    import capo_cleanrooms.types.collaboration_summary

    out: CollaborationSummaryList = []
    for item in data:
        out.append(capo_cleanrooms.types.collaboration_summary.deserialize_json(item))
    return out
