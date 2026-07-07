"""Generated from Smithy shape ``com.amazonaws.qapps#ConversationMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_qapps.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qapps.types.sender


class ConversationMessage(TypedDict, closed=True):
    body: "str"
    """<p>The text content of the conversation message.</p>"""
    type: "aws_sdk_qapps.types.sender.Sender"
    """<p>The type of the conversation message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConversationMessage) -> dict:
    out: dict = {}
    out["body"] = value["body"]
    import aws_sdk_qapps.types.sender

    out["type"] = aws_sdk_qapps.types.sender.serialize_json(value["type"])
    return out


def deserialize_json(data: dict) -> ConversationMessage:
    out: ConversationMessage = {}  # type: ignore[typeddict-item]
    if "body" in data:
        out["body"] = data["body"]
    else:
        raise DeserializationError("ConversationMessage.body required")
    if "type" in data:
        import aws_sdk_qapps.types.sender

        out["type"] = aws_sdk_qapps.types.sender.deserialize_json(data["type"])
    else:
        raise DeserializationError("ConversationMessage.type required")
    return out
