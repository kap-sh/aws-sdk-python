"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#TranscriptEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_lex_runtime_v2._protocol.eventstream import HeaderValue, Message

if TYPE_CHECKING:
    import aws_sdk_lex_runtime_v2.types.event_id
    import aws_sdk_lex_runtime_v2.types.string


class TranscriptEvent(TypedDict, closed=True):
    transcript: NotRequired["aws_sdk_lex_runtime_v2.types.string.String"]
    """<p>The transcript of the voice audio from the user.</p>"""
    event_id: NotRequired["aws_sdk_lex_runtime_v2.types.event_id.EventId"]
    """<p>A unique identifier of the event sent by Amazon Lex V2. The identifier is in the form <code>RESPONSE-N</code>, where N is a number starting with one and incremented for each event sent by Amazon Lex V2 in the current session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TranscriptEvent) -> dict:
    out: dict = {}
    if "transcript" in value:
        out["transcript"] = value["transcript"]
    if "event_id" in value:
        out["eventId"] = value["event_id"]
    return out


def deserialize_json(data: dict) -> TranscriptEvent:
    out: TranscriptEvent = {}  # type: ignore[typeddict-item]
    if "transcript" in data:
        out["transcript"] = data["transcript"]
    if "eventId" in data:
        out["event_id"] = data["eventId"]
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
