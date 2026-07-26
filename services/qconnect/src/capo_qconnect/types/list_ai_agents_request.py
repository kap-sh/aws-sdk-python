"""Generated from Smithy shape ``com.amazonaws.qconnect#ListAIAgentsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.max_results
    import capo_qconnect.types.next_token
    import capo_qconnect.types.origin
    import capo_qconnect.types.uuid_or_arn


class ListAIAgentsRequest(TypedDict, closed=True):
    assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    next_token: NotRequired["capo_qconnect.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""
    max_results: NotRequired["capo_qconnect.types.max_results.MaxResults"]
    """<p>The maximum number of results to return per page.</p>"""
    origin: NotRequired["capo_qconnect.types.origin.Origin"]
    """<p>The origin of the AI Agents to be listed. <code>SYSTEM</code> for a default AI Agent created by Q in Connect or <code>CUSTOMER</code> for an AI Agent created by calling AI Agent creation APIs. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAIAgentsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAIAgentsRequest:
    out: ListAIAgentsRequest = {}  # type: ignore[typeddict-item]
    return out
