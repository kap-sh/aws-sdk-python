"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#TextInputEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lex_runtime_v2._protocol.eventstream import HeaderValue, Message
from capo_lex_runtime_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_runtime_v2.types.epoch_millis
    import capo_lex_runtime_v2.types.event_id
    import capo_lex_runtime_v2.types.text


class TextInputEvent(TypedDict, closed=True):
    text: "capo_lex_runtime_v2.types.text.Text"
    """<p>The text from the user. Amazon Lex V2 processes this as a complete statement.</p>"""
    event_id: NotRequired["capo_lex_runtime_v2.types.event_id.EventId"]
    """<p>A unique identifier that your application assigns to the event. You can use this to identify events in logs.</p>"""
    client_timestamp_millis: "capo_lex_runtime_v2.types.epoch_millis.EpochMillis"
    """<p>A timestamp set by the client of the date and time that the event was sent to Amazon Lex V2.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TextInputEvent) -> dict:
    out: dict = {}
    out["text"] = value["text"]
    if "event_id" in value:
        out["eventId"] = value["event_id"]
    out["clientTimestampMillis"] = value.get("client_timestamp_millis", 0)
    return out


def deserialize_json(data: dict) -> TextInputEvent:
    out: TextInputEvent = {}  # type: ignore[typeddict-item]
    if "text" in data:
        out["text"] = data["text"]
    else:
        raise DeserializationError("TextInputEvent.text required")
    if "eventId" in data:
        out["event_id"] = data["eventId"]
    if "clientTimestampMillis" in data:
        out["client_timestamp_millis"] = data["clientTimestampMillis"]
    else:
        out["client_timestamp_millis"] = 0
    return out


def serialize_event_json(value: TextInputEvent) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "TextInputEvent"}
    payload = b""
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> TextInputEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: TextInputEvent = {}  # type: ignore[typeddict-item]
    return out
