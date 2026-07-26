"""Generated from Smithy shape ``com.amazonaws.connecthealth#MedicalScribeTranscriptEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connecthealth._protocol.eventstream import HeaderValue, Message

if TYPE_CHECKING:
    import capo_connecthealth.types.medical_scribe_transcript_segment


class MedicalScribeTranscriptEvent(TypedDict, closed=True):
    transcript_segment: NotRequired[
        "capo_connecthealth.types.medical_scribe_transcript_segment.MedicalScribeTranscriptSegment"
    ]
    """<p>A segment of the transcript</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MedicalScribeTranscriptEvent) -> dict:
    out: dict = {}
    if "transcript_segment" in value:
        import capo_connecthealth.types.medical_scribe_transcript_segment

        out["transcriptSegment"] = (
            capo_connecthealth.types.medical_scribe_transcript_segment.serialize_json(
                value["transcript_segment"]
            )
        )
    return out


def deserialize_json(data: dict) -> MedicalScribeTranscriptEvent:
    out: MedicalScribeTranscriptEvent = {}  # type: ignore[typeddict-item]
    if "transcriptSegment" in data:
        import capo_connecthealth.types.medical_scribe_transcript_segment

        out["transcript_segment"] = (
            capo_connecthealth.types.medical_scribe_transcript_segment.deserialize_json(
                data["transcriptSegment"]
            )
        )
    return out


def serialize_event_json(value: MedicalScribeTranscriptEvent) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "transcriptEvent"}
    payload = b""
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> MedicalScribeTranscriptEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: MedicalScribeTranscriptEvent = {}  # type: ignore[typeddict-item]
    return out
