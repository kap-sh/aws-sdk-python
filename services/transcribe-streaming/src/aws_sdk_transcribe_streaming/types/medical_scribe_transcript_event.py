"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#MedicalScribeTranscriptEvent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_transcribe_streaming._protocol.eventstream import HeaderValue, Message

if TYPE_CHECKING:
    import aws_sdk_transcribe_streaming.types.medical_scribe_transcript_segment


class MedicalScribeTranscriptEvent(TypedDict):
    transcript_segment: NotRequired[
        "aws_sdk_transcribe_streaming.types.medical_scribe_transcript_segment.MedicalScribeTranscriptSegment"
    ]
    """<p>The <code>TranscriptSegment</code> associated with a <code>MedicalScribeTranscriptEvent</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MedicalScribeTranscriptEvent) -> dict:
    out: dict = {}
    if "transcript_segment" in value:
        import aws_sdk_transcribe_streaming.types.medical_scribe_transcript_segment

        out["TranscriptSegment"] = (
            aws_sdk_transcribe_streaming.types.medical_scribe_transcript_segment.serialize_json(
                value["transcript_segment"]
            )
        )
    return out


def deserialize_json(data: dict) -> MedicalScribeTranscriptEvent:
    out: MedicalScribeTranscriptEvent = {}  # type: ignore[typeddict-item]
    if "TranscriptSegment" in data:
        import aws_sdk_transcribe_streaming.types.medical_scribe_transcript_segment

        out["transcript_segment"] = (
            aws_sdk_transcribe_streaming.types.medical_scribe_transcript_segment.deserialize_json(
                data["TranscriptSegment"]
            )
        )
    return out


def serialize_event_json(value: MedicalScribeTranscriptEvent) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "TranscriptEvent"}
    payload = b""
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> MedicalScribeTranscriptEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: MedicalScribeTranscriptEvent = {}  # type: ignore[typeddict-item]
    return out
