"""Generated from Smithy shape ``com.amazonaws.qbusiness#ListMessagesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.application_id
    import capo_qbusiness.types.conversation_id
    import capo_qbusiness.types.max_results_integer_for_list_messages
    import capo_qbusiness.types.next_token
    import capo_qbusiness.types.user_id


class ListMessagesRequest(TypedDict, closed=True):
    conversation_id: "capo_qbusiness.types.conversation_id.ConversationId"
    """<p>The identifier of the Amazon Q Business web experience conversation.</p>"""
    application_id: "capo_qbusiness.types.application_id.ApplicationId"
    """<p>The identifier for the Amazon Q Business application.</p>"""
    user_id: NotRequired["capo_qbusiness.types.user_id.UserId"]
    """<p>The identifier of the user involved in the Amazon Q Business web experience conversation.</p>"""
    next_token: NotRequired["capo_qbusiness.types.next_token.NextToken"]
    """<p>If the number of messages returned exceeds <code>maxResults</code>, Amazon Q Business returns a next token as a pagination token to retrieve the next set of messages.</p>"""
    max_results: NotRequired[
        "capo_qbusiness.types.max_results_integer_for_list_messages.MaxResultsIntegerForListMessages"
    ]
    """<p>The maximum number of messages to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMessagesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListMessagesRequest:
    out: ListMessagesRequest = {}  # type: ignore[typeddict-item]
    return out
