"""Generated from Smithy shape ``com.amazonaws.iotsitewise#InvokeAssistantResponse``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.conversation_id
    import aws_sdk_iotsitewise.types.response_stream


class InvokeAssistantResponse(TypedDict):
    body: "aws_sdk_iotsitewise.types.response_stream.ResponseStream"
    conversation_id: "aws_sdk_iotsitewise.types.conversation_id.ConversationId"
    """<p>The ID of the conversation, in UUID format. This ID uniquely identifies the conversation within IoT SiteWise.</p>"""
