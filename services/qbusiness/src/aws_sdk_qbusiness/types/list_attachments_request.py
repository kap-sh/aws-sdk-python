"""Generated from Smithy shape ``com.amazonaws.qbusiness#ListAttachmentsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.application_id
    import aws_sdk_qbusiness.types.conversation_id
    import aws_sdk_qbusiness.types.max_results_integer_for_list_attachments
    import aws_sdk_qbusiness.types.next_token
    import aws_sdk_qbusiness.types.user_id


class ListAttachmentsRequest(TypedDict):
    application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId"
    """<p>The unique identifier for the Amazon Q Business application.</p>"""
    conversation_id: NotRequired[
        "aws_sdk_qbusiness.types.conversation_id.ConversationId"
    ]
    """<p>The unique identifier of the Amazon Q Business web experience conversation.</p>"""
    user_id: NotRequired["aws_sdk_qbusiness.types.user_id.UserId"]
    """<p>The unique identifier of the user involved in the Amazon Q Business web experience conversation.</p>"""
    next_token: NotRequired["aws_sdk_qbusiness.types.next_token.NextToken"]
    """<p>If the number of attachments returned exceeds <code>maxResults</code>, Amazon Q Business returns a next token as a pagination token to retrieve the next set of attachments.</p>"""
    max_results: NotRequired[
        "aws_sdk_qbusiness.types.max_results_integer_for_list_attachments.MaxResultsIntegerForListAttachments"
    ]
    """<p>The maximum number of attachements to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAttachmentsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAttachmentsRequest:
    out: ListAttachmentsRequest = {}  # type: ignore[typeddict-item]
    return out
