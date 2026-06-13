"""Generated from Smithy shape ``com.amazonaws.cleanrooms#CollaborationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.collaboration_summary

CollaborationSummaryList: TypeAlias = list[
    "aws_sdk_cleanrooms.types.collaboration_summary.CollaborationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: CollaborationSummaryList) -> list:
    import aws_sdk_cleanrooms.types.collaboration_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_cleanrooms.types.collaboration_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> CollaborationSummaryList:
    import aws_sdk_cleanrooms.types.collaboration_summary

    out: CollaborationSummaryList = []
    for item in data:
        out.append(
            aws_sdk_cleanrooms.types.collaboration_summary.deserialize_json(item)
        )
    return out
