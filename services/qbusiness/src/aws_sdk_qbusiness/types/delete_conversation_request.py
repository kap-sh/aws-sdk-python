"""Generated from Smithy shape ``com.amazonaws.qbusiness#DeleteConversationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.application_id
    import aws_sdk_qbusiness.types.conversation_id
    import aws_sdk_qbusiness.types.user_id


class DeleteConversationRequest(TypedDict):
    conversation_id: "aws_sdk_qbusiness.types.conversation_id.ConversationId"
    """<p>The identifier of the Amazon Q Business web experience conversation being deleted.</p>"""
    application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId"
    """<p>The identifier of the Amazon Q Business application associated with the conversation.</p>"""
    user_id: NotRequired["aws_sdk_qbusiness.types.user_id.UserId"]
    """<p>The identifier of the user who is deleting the conversation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteConversationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteConversationRequest:
    out: DeleteConversationRequest = {}  # type: ignore[typeddict-item]
    return out
