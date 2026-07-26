"""Generated from Smithy shape ``com.amazonaws.qconnect#ListAIAgentVersionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.max_results
    import capo_qconnect.types.next_token
    import capo_qconnect.types.origin
    import capo_qconnect.types.uuid_or_arn
    import capo_qconnect.types.uuid_or_arn_or_either_with_qualifier


class ListAIAgentVersionsRequest(TypedDict, closed=True):
    assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    ai_agent_id: "capo_qconnect.types.uuid_or_arn_or_either_with_qualifier.UuidOrArnOrEitherWithQualifier"
    """<p>The identifier of the Amazon Q in Connect AI Agent for which versions are to be listed.</p>"""
    next_token: NotRequired["capo_qconnect.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""
    max_results: NotRequired["capo_qconnect.types.max_results.MaxResults"]
    """<p>The maximum number of results to return per page.</p>"""
    origin: NotRequired["capo_qconnect.types.origin.Origin"]
    """<p>The origin of the AI Agent versions to be listed. <code>SYSTEM</code> for a default AI Agent created by Q in Connect or <code>CUSTOMER</code> for an AI Agent created by calling AI Agent creation APIs. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAIAgentVersionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAIAgentVersionsRequest:
    out: ListAIAgentVersionsRequest = {}  # type: ignore[typeddict-item]
    return out
