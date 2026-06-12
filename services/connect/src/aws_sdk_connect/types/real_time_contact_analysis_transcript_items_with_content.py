"""Generated from Smithy shape ``com.amazonaws.connect#RealTimeContactAnalysisTranscriptItemsWithContent``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.real_time_contact_analysis_transcript_item_with_content

RealTimeContactAnalysisTranscriptItemsWithContent: TypeAlias = list[
    "aws_sdk_connect.types.real_time_contact_analysis_transcript_item_with_content.RealTimeContactAnalysisTranscriptItemWithContent"
]


# --- restJson1 ser/de ---
def serialize_json(value: RealTimeContactAnalysisTranscriptItemsWithContent) -> list:
    import aws_sdk_connect.types.real_time_contact_analysis_transcript_item_with_content

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connect.types.real_time_contact_analysis_transcript_item_with_content.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RealTimeContactAnalysisTranscriptItemsWithContent:
    import aws_sdk_connect.types.real_time_contact_analysis_transcript_item_with_content

    out: RealTimeContactAnalysisTranscriptItemsWithContent = []
    for item in data:
        out.append(
            aws_sdk_connect.types.real_time_contact_analysis_transcript_item_with_content.deserialize_json(
                item
            )
        )
    return out
