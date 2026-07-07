"""Generated from Smithy shape ``com.amazonaws.qbusiness#Conversation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.conversation_id
    import aws_sdk_qbusiness.types.conversation_title
    import aws_sdk_qbusiness.types.timestamp


class Conversation(TypedDict, closed=True):
    conversation_id: NotRequired[
        "aws_sdk_qbusiness.types.conversation_id.ConversationId"
    ]
    """<p>The identifier of the Amazon Q Business conversation.</p>"""
    title: NotRequired["aws_sdk_qbusiness.types.conversation_title.ConversationTitle"]
    """<p>The title of the conversation.</p>"""
    start_time: NotRequired["aws_sdk_qbusiness.types.timestamp.Timestamp"]
    """<p>The start time of the conversation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Conversation) -> dict:
    out: dict = {}
    if "conversation_id" in value:
        out["conversationId"] = value["conversation_id"]
    if "title" in value:
        out["title"] = value["title"]
    if "start_time" in value:
        import aws_sdk_qbusiness.types.timestamp

        out["startTime"] = aws_sdk_qbusiness.types.timestamp.serialize_json(
            value["start_time"]
        )
    return out


def deserialize_json(data: dict) -> Conversation:
    out: Conversation = {}  # type: ignore[typeddict-item]
    if "conversationId" in data:
        out["conversation_id"] = data["conversationId"]
    if "title" in data:
        out["title"] = data["title"]
    if "startTime" in data:
        import aws_sdk_qbusiness.types.timestamp

        out["start_time"] = aws_sdk_qbusiness.types.timestamp.deserialize_json(
            data["startTime"]
        )
    return out
