"""Generated from Smithy shape ``com.amazonaws.cleanrooms#CollaborationChangeRequestSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanrooms.types.collaboration_change_request_summary

CollaborationChangeRequestSummaryList: TypeAlias = list[
    "capo_cleanrooms.types.collaboration_change_request_summary.CollaborationChangeRequestSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: CollaborationChangeRequestSummaryList) -> list:
    import capo_cleanrooms.types.collaboration_change_request_summary

    out: list = []
    for item in value:
        out.append(
            capo_cleanrooms.types.collaboration_change_request_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CollaborationChangeRequestSummaryList:
    import capo_cleanrooms.types.collaboration_change_request_summary

    out: CollaborationChangeRequestSummaryList = []
    for item in data:
        out.append(
            capo_cleanrooms.types.collaboration_change_request_summary.deserialize_json(
                item
            )
        )
    return out
