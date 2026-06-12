"""Generated from Smithy shape ``com.amazonaws.connect#RealTimeContactAnalysisTranscriptItemsWithCharacterOffsets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.real_time_contact_analysis_transcript_item_with_character_offsets

RealTimeContactAnalysisTranscriptItemsWithCharacterOffsets: TypeAlias = list[
    "aws_sdk_connect.types.real_time_contact_analysis_transcript_item_with_character_offsets.RealTimeContactAnalysisTranscriptItemWithCharacterOffsets"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: RealTimeContactAnalysisTranscriptItemsWithCharacterOffsets,
) -> list:
    import aws_sdk_connect.types.real_time_contact_analysis_transcript_item_with_character_offsets

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connect.types.real_time_contact_analysis_transcript_item_with_character_offsets.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> RealTimeContactAnalysisTranscriptItemsWithCharacterOffsets:
    import aws_sdk_connect.types.real_time_contact_analysis_transcript_item_with_character_offsets

    out: RealTimeContactAnalysisTranscriptItemsWithCharacterOffsets = []
    for item in data:
        out.append(
            aws_sdk_connect.types.real_time_contact_analysis_transcript_item_with_character_offsets.deserialize_json(
                item
            )
        )
    return out
