"""Generated from Smithy shape ``com.amazonaws.qbusiness#TextInputEvent``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.user_message


class TextInputEvent(TypedDict):
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
