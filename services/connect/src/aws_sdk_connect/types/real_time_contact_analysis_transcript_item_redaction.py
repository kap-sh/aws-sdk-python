"""Generated from Smithy shape ``com.amazonaws.connect#RealTimeContactAnalysisTranscriptItemRedaction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.real_time_contact_analysis_character_intervals


class RealTimeContactAnalysisTranscriptItemRedaction(TypedDict, closed=True):
    character_offsets: NotRequired[
        "aws_sdk_connect.types.real_time_contact_analysis_character_intervals.RealTimeContactAnalysisCharacterIntervals"
    ]
    """<p>List of character intervals each describing a part of the text that was redacted. For <code>OutputType.Raw</code>, part of the original text that contains data that can be redacted. For <code> OutputType.Redacted</code>, part of the string with redaction tag.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RealTimeContactAnalysisTranscriptItemRedaction) -> dict:
    out: dict = {}
    if "character_offsets" in value:
        import aws_sdk_connect.types.real_time_contact_analysis_character_intervals

        out["CharacterOffsets"] = (
            aws_sdk_connect.types.real_time_contact_analysis_character_intervals.serialize_json(
                value["character_offsets"]
            )
        )
    return out


def deserialize_json(data: dict) -> RealTimeContactAnalysisTranscriptItemRedaction:
    out: RealTimeContactAnalysisTranscriptItemRedaction = {}  # type: ignore[typeddict-item]
    if "CharacterOffsets" in data:
        import aws_sdk_connect.types.real_time_contact_analysis_character_intervals

        out["character_offsets"] = (
            aws_sdk_connect.types.real_time_contact_analysis_character_intervals.deserialize_json(
                data["CharacterOffsets"]
            )
        )
    return out
