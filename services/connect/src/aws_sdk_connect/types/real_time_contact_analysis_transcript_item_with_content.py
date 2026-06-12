"""Generated from Smithy shape ``com.amazonaws.connect#RealTimeContactAnalysisTranscriptItemWithContent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.real_time_contact_analysis_character_interval
    import aws_sdk_connect.types.real_time_contact_analysis_id256
    import aws_sdk_connect.types.real_time_contact_analysis_transcript_content


class RealTimeContactAnalysisTranscriptItemWithContent(TypedDict):
    content: NotRequired[
        "aws_sdk_connect.types.real_time_contact_analysis_transcript_content.RealTimeContactAnalysisTranscriptContent"
    ]
    """<p>Part of the transcript content that contains identified issue. Can be redacted</p>"""
    id: "aws_sdk_connect.types.real_time_contact_analysis_id256.RealTimeContactAnalysisId256"
    """<p>Transcript identifier. Matches the identifier from one of the TranscriptSegments.</p>"""
    character_offsets: NotRequired[
        "aws_sdk_connect.types.real_time_contact_analysis_character_interval.RealTimeContactAnalysisCharacterInterval"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: RealTimeContactAnalysisTranscriptItemWithContent) -> dict:
    out: dict = {}
    if "content" in value:
        out["Content"] = value["content"]
    out["Id"] = value["id"]
    if "character_offsets" in value:
        import aws_sdk_connect.types.real_time_contact_analysis_character_interval

        out["CharacterOffsets"] = (
            aws_sdk_connect.types.real_time_contact_analysis_character_interval.serialize_json(
                value["character_offsets"]
            )
        )
    return out


def deserialize_json(data: dict) -> RealTimeContactAnalysisTranscriptItemWithContent:
    out: RealTimeContactAnalysisTranscriptItemWithContent = {}  # type: ignore[typeddict-item]
    if "Content" in data:
        out["content"] = data["Content"]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError(
            "RealTimeContactAnalysisTranscriptItemWithContent.id required"
        )
    if "CharacterOffsets" in data:
        import aws_sdk_connect.types.real_time_contact_analysis_character_interval

        out["character_offsets"] = (
            aws_sdk_connect.types.real_time_contact_analysis_character_interval.deserialize_json(
                data["CharacterOffsets"]
            )
        )
    return out
