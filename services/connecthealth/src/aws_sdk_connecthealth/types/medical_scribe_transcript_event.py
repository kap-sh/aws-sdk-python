"""Generated from Smithy shape ``com.amazonaws.connecthealth#MedicalScribeTranscriptEvent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connecthealth.types.medical_scribe_transcript_segment


class MedicalScribeTranscriptEvent(TypedDict):
    transcript_segment: NotRequired[
        "aws_sdk_connecthealth.types.medical_scribe_transcript_segment.MedicalScribeTranscriptSegment"
    ]
    """<p>A segment of the transcript</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MedicalScribeTranscriptEvent) -> dict:
    out: dict = {}
    if "transcript_segment" in value:
        import aws_sdk_connecthealth.types.medical_scribe_transcript_segment

        out["transcriptSegment"] = (
            aws_sdk_connecthealth.types.medical_scribe_transcript_segment.serialize_json(
                value["transcript_segment"]
            )
        )
    return out


def deserialize_json(data: dict) -> MedicalScribeTranscriptEvent:
    out: MedicalScribeTranscriptEvent = {}  # type: ignore[typeddict-item]
    if "transcriptSegment" in data:
        import aws_sdk_connecthealth.types.medical_scribe_transcript_segment

        out["transcript_segment"] = (
            aws_sdk_connecthealth.types.medical_scribe_transcript_segment.deserialize_json(
                data["transcriptSegment"]
            )
        )
    return out
