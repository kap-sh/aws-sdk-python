"""Generated from Smithy shape ``com.amazonaws.qbusiness#TextInputEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_qbusiness._protocol.eventstream import HeaderValue, Message
from aws_sdk_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.user_message


class TextInputEvent(TypedDict, closed=True):
    user_message: "aws_sdk_qbusiness.types.user_message.UserMessage"
    """<p>A user message in a text message input event.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TextInputEvent) -> dict:
    out: dict = {}
    out["userMessage"] = value["user_message"]
    return out


def deserialize_json(data: dict) -> TextInputEvent:
    out: TextInputEvent = {}  # type: ignore[typeddict-item]
    if "userMessage" in data:
        out["user_message"] = data["userMessage"]
    else:
        raise DeserializationError("TextInputEvent.user_message required")
    return out


def serialize_event_json(value: TextInputEvent) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "textEvent"}
    payload = b""
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> TextInputEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: TextInputEvent = {}  # type: ignore[typeddict-item]
    return out
