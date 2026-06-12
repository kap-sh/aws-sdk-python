"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#GetAgentMemoryRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.agent_alias_id
    import aws_sdk_bedrock_agent_runtime.types.agent_id
    import aws_sdk_bedrock_agent_runtime.types.max_results
    import aws_sdk_bedrock_agent_runtime.types.memory_id
    import aws_sdk_bedrock_agent_runtime.types.memory_type
    import aws_sdk_bedrock_agent_runtime.types.next_token

class GetAgentMemoryRequest(TypedDict):
    next_token: NotRequired["aws_sdk_bedrock_agent_runtime.types.next_token.NextToken"]
    """<p>If the total number of results is greater than the maxItems value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>"""
    max_items: NotRequired["aws_sdk_bedrock_agent_runtime.types.max_results.MaxResults"]
    """<p>The maximum number of items to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>"""
    agent_id: "aws_sdk_bedrock_agent_runtime.types.agent_id.AgentId"
    """<p>The unique identifier of the agent to which the alias belongs.</p>"""
    agent_alias_id: "aws_sdk_bedrock_agent_runtime.types.agent_alias_id.AgentAliasId"
    """<p>The unique identifier of an alias of an agent.</p>"""
    memory_type: "aws_sdk_bedrock_agent_runtime.types.memory_type.MemoryType"
    """<p>The type of memory.</p>"""
    memory_id: "aws_sdk_bedrock_agent_runtime.types.memory_id.MemoryId"
    """<p>The unique identifier of the memory. </p>"""

# --- restJson1 ser/de ---
def serialize_json(value: GetAgentMemoryRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAgentMemoryRequest:
    out: GetAgentMemoryRequest = {}  # type: ignore[typeddict-item]
    return out