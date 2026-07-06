"""Generated from Smithy shape ``com.amazonaws.iotsitewise#InvokeAssistantRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.conversation_id
    import aws_sdk_iotsitewise.types.message_input


class InvokeAssistantRequest(TypedDict, closed=True):
    conversation_id: NotRequired[
        "aws_sdk_iotsitewise.types.conversation_id.ConversationId"
    ]
    """<p>The ID assigned to a conversation. IoT SiteWise automatically generates a unique ID for you, and this parameter is never required. However, if you prefer to have your own ID, you must specify it here in UUID format. If you specify your own ID, it must be globally unique.</p>"""
    message: "aws_sdk_iotsitewise.types.message_input.MessageInput"
    """<p>A text message sent to the SiteWise Assistant by the user.</p>"""
    enable_trace: "bool"
    """<p>Specifies if to turn trace on or not. It is used to track the SiteWise Assistant's reasoning, and data access process.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvokeAssistantRequest) -> dict:
    out: dict = {}
    if "conversation_id" in value:
        out["conversationId"] = value["conversation_id"]
    out["message"] = value["message"]
    out["enableTrace"] = value.get("enable_trace", False)
    return out


def deserialize_json(data: dict) -> InvokeAssistantRequest:
    out: InvokeAssistantRequest = {}  # type: ignore[typeddict-item]
    if "conversationId" in data:
        out["conversation_id"] = data["conversationId"]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("InvokeAssistantRequest.message required")
    if "enableTrace" in data:
        out["enable_trace"] = data["enableTrace"]
    else:
        out["enable_trace"] = False
    return out
