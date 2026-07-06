"""Generated from Smithy shape ``com.amazonaws.iotsitewise#Trace``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iotsitewise._protocol.eventstream import HeaderValue, Message

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.string


class Trace(TypedDict, closed=True):
    text: NotRequired["aws_sdk_iotsitewise.types.string.String"]
    """<p>The cited text from the data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Trace) -> dict:
    out: dict = {}
    if "text" in value:
        out["text"] = value["text"]
    return out


def deserialize_json(data: dict) -> Trace:
    out: Trace = {}  # type: ignore[typeddict-item]
    if "text" in data:
        out["text"] = data["text"]
    return out


def serialize_event_json(value: Trace) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "trace"}
    payload = b""
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> Trace:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: Trace = {}  # type: ignore[typeddict-item]
    return out
