"""Generated from Smithy shape ``com.amazonaws.qbusiness#TextOutputEvent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_qbusiness._protocol.eventstream import HeaderValue, Message

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.conversation_id
    import aws_sdk_qbusiness.types.message_id
    import aws_sdk_qbusiness.types.string
    import aws_sdk_qbusiness.types.system_message_type


class TextOutputEvent(TypedDict):
    system_message_type: NotRequired[
        "aws_sdk_qbusiness.types.system_message_type.SystemMessageType"
    ]
    """<p>The type of AI-generated message in a <code>TextOutputEvent</code>. Amazon Q Business currently supports two types of messages:</p> <ul> <li> <p> <code>RESPONSE</code> - The Amazon Q Business system response.</p> </li> <li> <p> <code>GROUNDED_RESPONSE</code> - The corrected, hallucination-reduced, response returned by Amazon Q Business. Available only if hallucination reduction is supported and configured for the application and detected in the end user chat query by Amazon Q Business.</p> </li> </ul>"""
    conversation_id: NotRequired[
        "aws_sdk_qbusiness.types.conversation_id.ConversationId"
    ]
    """<p>The identifier of the conversation with which the text output event is associated.</p>"""
    user_message_id: NotRequired["aws_sdk_qbusiness.types.message_id.MessageId"]
    """<p>The identifier of an end user message in a <code>TextOutputEvent</code>.</p>"""
    system_message_id: NotRequired["aws_sdk_qbusiness.types.message_id.MessageId"]
    """<p>The identifier of an AI-generated message in a <code>TextOutputEvent</code>.</p>"""
    system_message: NotRequired["aws_sdk_qbusiness.types.string.String"]
    """<p>An AI-generated message in a <code>TextOutputEvent</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TextOutputEvent) -> dict:
    out: dict = {}
    if "system_message_type" in value:
        import aws_sdk_qbusiness.types.system_message_type

        out["systemMessageType"] = (
            aws_sdk_qbusiness.types.system_message_type.serialize_json(
                value["system_message_type"]
            )
        )
    if "conversation_id" in value:
        out["conversationId"] = value["conversation_id"]
    if "user_message_id" in value:
        out["userMessageId"] = value["user_message_id"]
    if "system_message_id" in value:
        out["systemMessageId"] = value["system_message_id"]
    if "system_message" in value:
        out["systemMessage"] = value["system_message"]
    return out


def deserialize_json(data: dict) -> TextOutputEvent:
    out: TextOutputEvent = {}  # type: ignore[typeddict-item]
    if "systemMessageType" in data:
        import aws_sdk_qbusiness.types.system_message_type

        out["system_message_type"] = (
            aws_sdk_qbusiness.types.system_message_type.deserialize_json(
                data["systemMessageType"]
            )
        )
    if "conversationId" in data:
        out["conversation_id"] = data["conversationId"]
    if "userMessageId" in data:
        out["user_message_id"] = data["userMessageId"]
    if "systemMessageId" in data:
        out["system_message_id"] = data["systemMessageId"]
    if "systemMessage" in data:
        out["system_message"] = data["systemMessage"]
    return out


def serialize_event_json(value: TextOutputEvent) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "textEvent"}
    payload = b""
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> TextOutputEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: TextOutputEvent = {}  # type: ignore[typeddict-item]
    return out
