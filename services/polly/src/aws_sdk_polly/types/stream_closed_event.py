"""Generated from Smithy shape ``com.amazonaws.polly#StreamClosedEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_polly._protocol.eventstream import HeaderValue, Message

if TYPE_CHECKING:
    import aws_sdk_polly.types.request_characters


class StreamClosedEvent(TypedDict, closed=True):
    request_characters: "aws_sdk_polly.types.request_characters.RequestCharacters"
    """<p>The total number of characters synthesized during the streaming session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StreamClosedEvent) -> dict:
    out: dict = {}
    out["RequestCharacters"] = value.get("request_characters", 0)
    return out


def deserialize_json(data: dict) -> StreamClosedEvent:
    out: StreamClosedEvent = {}  # type: ignore[typeddict-item]
    if "RequestCharacters" in data:
        out["request_characters"] = data["RequestCharacters"]
    else:
        out["request_characters"] = 0
    return out


def serialize_event_json(value: StreamClosedEvent) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "StreamClosedEvent"}
    payload = b""
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> StreamClosedEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: StreamClosedEvent = {}  # type: ignore[typeddict-item]
    return out
