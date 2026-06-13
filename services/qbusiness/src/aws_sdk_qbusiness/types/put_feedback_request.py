"""Generated from Smithy shape ``com.amazonaws.qbusiness#PutFeedbackRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.application_id
    import aws_sdk_qbusiness.types.conversation_id
    import aws_sdk_qbusiness.types.message_usefulness_feedback
    import aws_sdk_qbusiness.types.system_message_id
    import aws_sdk_qbusiness.types.timestamp
    import aws_sdk_qbusiness.types.user_id


class PutFeedbackRequest(TypedDict):
    application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId"
    """<p>The identifier of the application associated with the feedback.</p>"""
    user_id: NotRequired["aws_sdk_qbusiness.types.user_id.UserId"]
    """<p>The identifier of the user giving the feedback.</p>"""
    conversation_id: "aws_sdk_qbusiness.types.conversation_id.ConversationId"
    """<p>The identifier of the conversation the feedback is attached to.</p>"""
    message_id: "aws_sdk_qbusiness.types.system_message_id.SystemMessageId"
    """<p>The identifier of the chat message that the feedback was given for.</p>"""
    message_copied_at: NotRequired["aws_sdk_qbusiness.types.timestamp.Timestamp"]
    """<p>The timestamp for when the feedback was recorded.</p>"""
    message_usefulness: NotRequired[
        "aws_sdk_qbusiness.types.message_usefulness_feedback.MessageUsefulnessFeedback"
    ]
    """<p>The feedback usefulness value given by the user to the chat message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutFeedbackRequest) -> dict:
    out: dict = {}
    if "message_copied_at" in value:
        import aws_sdk_qbusiness.types.timestamp

        out["messageCopiedAt"] = aws_sdk_qbusiness.types.timestamp.serialize_json(
            value["message_copied_at"]
        )
    if "message_usefulness" in value:
        import aws_sdk_qbusiness.types.message_usefulness_feedback

        out["messageUsefulness"] = (
            aws_sdk_qbusiness.types.message_usefulness_feedback.serialize_json(
                value["message_usefulness"]
            )
        )
    return out


def deserialize_json(data: dict) -> PutFeedbackRequest:
    out: PutFeedbackRequest = {}  # type: ignore[typeddict-item]
    if "messageCopiedAt" in data:
        import aws_sdk_qbusiness.types.timestamp

        out["message_copied_at"] = aws_sdk_qbusiness.types.timestamp.deserialize_json(
            data["messageCopiedAt"]
        )
    if "messageUsefulness" in data:
        import aws_sdk_qbusiness.types.message_usefulness_feedback

        out["message_usefulness"] = (
            aws_sdk_qbusiness.types.message_usefulness_feedback.deserialize_json(
                data["messageUsefulness"]
            )
        )
    return out
