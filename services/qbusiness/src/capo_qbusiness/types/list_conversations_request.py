"""Generated from Smithy shape ``com.amazonaws.qbusiness#ListConversationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.application_id
    import capo_qbusiness.types.max_results_integer_for_list_conversations
    import capo_qbusiness.types.next_token
    import capo_qbusiness.types.user_id


class ListConversationsRequest(TypedDict, closed=True):
    application_id: "capo_qbusiness.types.application_id.ApplicationId"
    """<p>The identifier of the Amazon Q Business application.</p>"""
    user_id: NotRequired["capo_qbusiness.types.user_id.UserId"]
    """<p>The identifier of the user involved in the Amazon Q Business web experience conversation. </p>"""
    next_token: NotRequired["capo_qbusiness.types.next_token.NextToken"]
    """<p>If the <code>maxResults</code> response was incomplete because there is more data to retrieve, Amazon Q Business returns a pagination token in the response. You can use this pagination token to retrieve the next set of Amazon Q Business conversations.</p>"""
    max_results: NotRequired[
        "capo_qbusiness.types.max_results_integer_for_list_conversations.MaxResultsIntegerForListConversations"
    ]
    """<p>The maximum number of Amazon Q Business conversations to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListConversationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListConversationsRequest:
    out: ListConversationsRequest = {}  # type: ignore[typeddict-item]
    return out
