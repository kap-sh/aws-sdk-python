"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#PlaybackCompletionEvent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lex_runtime_v2._protocol.eventstream import HeaderValue, Message

if TYPE_CHECKING:
    import aws_sdk_lex_runtime_v2.types.epoch_millis
    import aws_sdk_lex_runtime_v2.types.event_id


class PlaybackCompletionEvent(TypedDict):
    event_id: NotRequired["aws_sdk_lex_runtime_v2.types.event_id.EventId"]
    """<p>A unique identifier that your application assigns to the event. You can use this to identify events in logs.</p>"""
    client_timestamp_millis: "aws_sdk_lex_runtime_v2.types.epoch_millis.EpochMillis"
    """<p>A timestamp set by the client of the date and time that the event was sent to Amazon Lex V2.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PlaybackCompletionEvent) -> dict:
    out: dict = {}
    if "event_id" in value:
        out["eventId"] = value["event_id"]
    out["clientTimestampMillis"] = value.get("client_timestamp_millis", 0)
    return out


def deserialize_json(data: dict) -> PlaybackCompletionEvent:
    out: PlaybackCompletionEvent = {}  # type: ignore[typeddict-item]
    if "eventId" in data:
        out["event_id"] = data["eventId"]
    if "clientTimestampMillis" in data:
        out["client_timestamp_millis"] = data["clientTimestampMillis"]
    else:
        out["client_timestamp_millis"] = 0
    return out


def serialize_event_json(value: PlaybackCompletionEvent) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "PlaybackCompletionEvent"}
    payload = b""
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> PlaybackCompletionEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: PlaybackCompletionEvent = {}  # type: ignore[typeddict-item]
    return out
