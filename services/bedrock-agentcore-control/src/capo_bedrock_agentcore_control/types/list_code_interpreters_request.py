"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListCodeInterpretersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.max_results
    import capo_bedrock_agentcore_control.types.next_token
    import capo_bedrock_agentcore_control.types.resource_type


class ListCodeInterpretersRequest(TypedDict, closed=True):
    max_results: NotRequired[
        "capo_bedrock_agentcore_control.types.max_results.MaxResults"
    ]
    """<p>The maximum number of results to return in the response.</p>"""
    next_token: NotRequired["capo_bedrock_agentcore_control.types.next_token.NextToken"]
    """<p>A token to retrieve the next page of results.</p>"""
    type: NotRequired["capo_bedrock_agentcore_control.types.resource_type.ResourceType"]
    """<p>The type of code interpreters to list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCodeInterpretersRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListCodeInterpretersRequest:
    out: ListCodeInterpretersRequest = {}  # type: ignore[typeddict-item]
    return out
