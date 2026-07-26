"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListAgentRuntimeVersionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.agent_runtime_id
    import capo_bedrock_agentcore_control.types.max_results
    import capo_bedrock_agentcore_control.types.next_token


class ListAgentRuntimeVersionsRequest(TypedDict, closed=True):
    agent_runtime_id: (
        "capo_bedrock_agentcore_control.types.agent_runtime_id.AgentRuntimeId"
    )
    """<p>The unique identifier of the AgentCore Runtime to list versions for.</p>"""
    max_results: NotRequired[
        "capo_bedrock_agentcore_control.types.max_results.MaxResults"
    ]
    """<p>The maximum number of results to return in the response.</p>"""
    next_token: NotRequired["capo_bedrock_agentcore_control.types.next_token.NextToken"]
    """<p>A token to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAgentRuntimeVersionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAgentRuntimeVersionsRequest:
    out: ListAgentRuntimeVersionsRequest = {}  # type: ignore[typeddict-item]
    return out
