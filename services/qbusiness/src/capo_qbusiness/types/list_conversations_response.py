"""Generated from Smithy shape ``com.amazonaws.qbusiness#ListConversationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.conversations
    import capo_qbusiness.types.next_token


class ListConversationsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_qbusiness.types.next_token.NextToken"]
    """<p>If the response is truncated, Amazon Q Business returns this token, which you can use in a later request to list the next set of messages.</p>"""
    conversations: NotRequired["capo_qbusiness.types.conversations.Conversations"]
    """<p>An array of summary information on the configuration of one or more Amazon Q Business web experiences.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListConversationsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "conversations" in value:
        import capo_qbusiness.types.conversations

        out["conversations"] = capo_qbusiness.types.conversations.serialize_json(
            value["conversations"]
        )
    return out


def deserialize_json(data: dict) -> ListConversationsResponse:
    out: ListConversationsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "conversations" in data:
        import capo_qbusiness.types.conversations

        out["conversations"] = capo_qbusiness.types.conversations.deserialize_json(
            data["conversations"]
        )
    return out
