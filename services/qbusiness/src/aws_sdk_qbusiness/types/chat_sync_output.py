"""Generated from Smithy shape ``com.amazonaws.qbusiness#ChatSyncOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.action_review
    import aws_sdk_qbusiness.types.attachments_output
    import aws_sdk_qbusiness.types.auth_challenge_request
    import aws_sdk_qbusiness.types.conversation_id
    import aws_sdk_qbusiness.types.message_id
    import aws_sdk_qbusiness.types.source_attributions
    import aws_sdk_qbusiness.types.string


class ChatSyncOutput(TypedDict, closed=True):
    conversation_id: NotRequired[
        "aws_sdk_qbusiness.types.conversation_id.ConversationId"
    ]
    """<p>The identifier of the Amazon Q Business conversation.</p>"""
    system_message: NotRequired["aws_sdk_qbusiness.types.string.String"]
    """<p>An AI-generated message in a conversation.</p>"""
    system_message_id: NotRequired["aws_sdk_qbusiness.types.message_id.MessageId"]
    """<p>The identifier of an Amazon Q Business AI generated message within the conversation.</p>"""
    user_message_id: NotRequired["aws_sdk_qbusiness.types.message_id.MessageId"]
    """<p>The identifier of an Amazon Q Business end user text input message within the conversation.</p>"""
    action_review: NotRequired["aws_sdk_qbusiness.types.action_review.ActionReview"]
    """<p>A request from Amazon Q Business to the end user for information Amazon Q Business needs to successfully complete a requested plugin action.</p>"""
    auth_challenge_request: NotRequired[
        "aws_sdk_qbusiness.types.auth_challenge_request.AuthChallengeRequest"
    ]
    """<p>An authentication verification event activated by an end user request to use a custom plugin.</p>"""
    source_attributions: NotRequired[
        "aws_sdk_qbusiness.types.source_attributions.SourceAttributions"
    ]
    """<p>The source documents used to generate the conversation response.</p>"""
    failed_attachments: NotRequired[
        "aws_sdk_qbusiness.types.attachments_output.AttachmentsOutput"
    ]
    """<p>A list of files which failed to upload during chat.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChatSyncOutput) -> dict:
    out: dict = {}
    if "conversation_id" in value:
        out["conversationId"] = value["conversation_id"]
    if "system_message" in value:
        out["systemMessage"] = value["system_message"]
    if "system_message_id" in value:
        out["systemMessageId"] = value["system_message_id"]
    if "user_message_id" in value:
        out["userMessageId"] = value["user_message_id"]
    if "action_review" in value:
        import aws_sdk_qbusiness.types.action_review

        out["actionReview"] = aws_sdk_qbusiness.types.action_review.serialize_json(
            value["action_review"]
        )
    if "auth_challenge_request" in value:
        import aws_sdk_qbusiness.types.auth_challenge_request

        out["authChallengeRequest"] = (
            aws_sdk_qbusiness.types.auth_challenge_request.serialize_json(
                value["auth_challenge_request"]
            )
        )
    if "source_attributions" in value:
        import aws_sdk_qbusiness.types.source_attributions

        out["sourceAttributions"] = (
            aws_sdk_qbusiness.types.source_attributions.serialize_json(
                value["source_attributions"]
            )
        )
    if "failed_attachments" in value:
        import aws_sdk_qbusiness.types.attachments_output

        out["failedAttachments"] = (
            aws_sdk_qbusiness.types.attachments_output.serialize_json(
                value["failed_attachments"]
            )
        )
    return out


def deserialize_json(data: dict) -> ChatSyncOutput:
    out: ChatSyncOutput = {}  # type: ignore[typeddict-item]
    if "conversationId" in data:
        out["conversation_id"] = data["conversationId"]
    if "systemMessage" in data:
        out["system_message"] = data["systemMessage"]
    if "systemMessageId" in data:
        out["system_message_id"] = data["systemMessageId"]
    if "userMessageId" in data:
        out["user_message_id"] = data["userMessageId"]
    if "actionReview" in data:
        import aws_sdk_qbusiness.types.action_review

        out["action_review"] = aws_sdk_qbusiness.types.action_review.deserialize_json(
            data["actionReview"]
        )
    if "authChallengeRequest" in data:
        import aws_sdk_qbusiness.types.auth_challenge_request

        out["auth_challenge_request"] = (
            aws_sdk_qbusiness.types.auth_challenge_request.deserialize_json(
                data["authChallengeRequest"]
            )
        )
    if "sourceAttributions" in data:
        import aws_sdk_qbusiness.types.source_attributions

        out["source_attributions"] = (
            aws_sdk_qbusiness.types.source_attributions.deserialize_json(
                data["sourceAttributions"]
            )
        )
    if "failedAttachments" in data:
        import aws_sdk_qbusiness.types.attachments_output

        out["failed_attachments"] = (
            aws_sdk_qbusiness.types.attachments_output.deserialize_json(
                data["failedAttachments"]
            )
        )
    return out
