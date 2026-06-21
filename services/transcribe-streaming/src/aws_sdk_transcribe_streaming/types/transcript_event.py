"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#TranscriptEvent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_transcribe_streaming._protocol.eventstream import HeaderValue, Message

if TYPE_CHECKING:
    import aws_sdk_transcribe_streaming.types.transcript


class TranscriptEvent(TypedDict):
    transcript: NotRequired["aws_sdk_transcribe_streaming.types.transcript.Transcript"]
    """<p>Contains <code>Results</code>, which contains a set of transcription results from one or more audio segments, along with additional information per your request parameters. This can include information relating to alternative transcriptions, channel identification, partial result stabilization, language identification, and other transcription-related data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TranscriptEvent) -> dict:
    out: dict = {}
    if "transcript" in value:
        import aws_sdk_transcribe_streaming.types.transcript

        out["Transcript"] = (
            aws_sdk_transcribe_streaming.types.transcript.serialize_json(
                value["transcript"]
            )
        )
    return out


def deserialize_json(data: dict) -> TranscriptEvent:
    out: TranscriptEvent = {}  # type: ignore[typeddict-item]
    if "Transcript" in data:
        import aws_sdk_transcribe_streaming.types.transcript

        out["transcript"] = (
            aws_sdk_transcribe_streaming.types.transcript.deserialize_json(
                data["Transcript"]
            )
        )
    return out


def serialize_event_json(value: TranscriptEvent) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "TranscriptEvent"}
    payload = b""
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> TranscriptEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: TranscriptEvent = {}  # type: ignore[typeddict-item]
    return out
