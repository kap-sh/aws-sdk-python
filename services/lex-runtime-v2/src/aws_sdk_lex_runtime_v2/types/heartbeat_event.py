"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#HeartbeatEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_lex_runtime_v2._protocol.eventstream import HeaderValue, Message

if TYPE_CHECKING:
    import aws_sdk_lex_runtime_v2.types.event_id


class HeartbeatEvent(TypedDict, closed=True):
    event_id: NotRequired["aws_sdk_lex_runtime_v2.types.event_id.EventId"]
    """<p>A unique identifier of the event sent by Amazon Lex V2. The identifier is in the form <code>RESPONSE-N</code>, where N is a number starting with one and incremented for each event sent by Amazon Lex V2 in the current session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HeartbeatEvent) -> dict:
    out: dict = {}
    if "event_id" in value:
        out["eventId"] = value["event_id"]
    return out


def deserialize_json(data: dict) -> HeartbeatEvent:
    out: HeartbeatEvent = {}  # type: ignore[typeddict-item]
    if "eventId" in data:
        out["event_id"] = data["eventId"]
    return out


def serialize_event_json(value: HeartbeatEvent) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "HeartbeatEvent"}
    payload = b""
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> HeartbeatEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: HeartbeatEvent = {}  # type: ignore[typeddict-item]
    return out
