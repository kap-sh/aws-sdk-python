"""Generated from Smithy shape ``com.amazonaws.connect#RealTimeContactAnalysisTranscriptItemsWithContent``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.real_time_contact_analysis_transcript_item_with_content

RealTimeContactAnalysisTranscriptItemsWithContent: TypeAlias = list[
    "capo_connect.types.real_time_contact_analysis_transcript_item_with_content.RealTimeContactAnalysisTranscriptItemWithContent"
]


# --- restJson1 ser/de ---
def serialize_json(value: RealTimeContactAnalysisTranscriptItemsWithContent) -> list:
    import capo_connect.types.real_time_contact_analysis_transcript_item_with_content

    out: list = []
    for item in value:
        out.append(
            capo_connect.types.real_time_contact_analysis_transcript_item_with_content.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RealTimeContactAnalysisTranscriptItemsWithContent:
    import capo_connect.types.real_time_contact_analysis_transcript_item_with_content

    out: RealTimeContactAnalysisTranscriptItemsWithContent = []
    for item in data:
        out.append(
            capo_connect.types.real_time_contact_analysis_transcript_item_with_content.deserialize_json(
                item
            )
        )
    return out
