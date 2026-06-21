"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#PlaybackInterruptionEvent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lex_runtime_v2._protocol.eventstream import HeaderValue, Message

if TYPE_CHECKING:
    import aws_sdk_lex_runtime_v2.types.event_id
    import aws_sdk_lex_runtime_v2.types.playback_interruption_reason


class PlaybackInterruptionEvent(TypedDict):
    event_reason: NotRequired[
        "aws_sdk_lex_runtime_v2.types.playback_interruption_reason.PlaybackInterruptionReason"
    ]
    """<p>Indicates the type of user input that Amazon Lex V2 detected.</p>"""
    caused_by_event_id: NotRequired["aws_sdk_lex_runtime_v2.types.event_id.EventId"]
    """<p>The identifier of the event that contained the audio, DTMF, or text that caused the interruption.</p>"""
    event_id: NotRequired["aws_sdk_lex_runtime_v2.types.event_id.EventId"]
    """<p>A unique identifier of the event sent by Amazon Lex V2. The identifier is in the form <code>RESPONSE-N</code>, where N is a number starting with one and incremented for each event sent by Amazon Lex V2 in the current session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PlaybackInterruptionEvent) -> dict:
    out: dict = {}
    if "event_reason" in value:
        import aws_sdk_lex_runtime_v2.types.playback_interruption_reason

        out["eventReason"] = (
            aws_sdk_lex_runtime_v2.types.playback_interruption_reason.serialize_json(
                value["event_reason"]
            )
        )
    if "caused_by_event_id" in value:
        out["causedByEventId"] = value["caused_by_event_id"]
    if "event_id" in value:
        out["eventId"] = value["event_id"]
    return out


def deserialize_json(data: dict) -> PlaybackInterruptionEvent:
    out: PlaybackInterruptionEvent = {}  # type: ignore[typeddict-item]
    if "eventReason" in data:
        import aws_sdk_lex_runtime_v2.types.playback_interruption_reason

        out["event_reason"] = (
            aws_sdk_lex_runtime_v2.types.playback_interruption_reason.deserialize_json(
                data["eventReason"]
            )
        )
    if "causedByEventId" in data:
        out["caused_by_event_id"] = data["causedByEventId"]
    if "eventId" in data:
        out["event_id"] = data["eventId"]
    return out


def serialize_event_json(value: PlaybackInterruptionEvent) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "PlaybackInterruptionEvent"}
    payload = b""
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> PlaybackInterruptionEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: PlaybackInterruptionEvent = {}  # type: ignore[typeddict-item]
    return out
