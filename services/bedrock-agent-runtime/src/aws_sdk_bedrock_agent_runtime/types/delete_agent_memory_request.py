"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#DeleteAgentMemoryRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.agent_alias_id
    import aws_sdk_bedrock_agent_runtime.types.agent_id
    import aws_sdk_bedrock_agent_runtime.types.memory_id
    import aws_sdk_bedrock_agent_runtime.types.session_id

class DeleteAgentMemoryRequest(TypedDict):
    agent_id: "aws_sdk_bedrock_agent_runtime.types.agent_id.AgentId"
    """<p>The unique identifier of the agent to which the alias belongs.</p>"""
    agent_alias_id: "aws_sdk_bedrock_agent_runtime.types.agent_alias_id.AgentAliasId"
    """<p>The unique identifier of an alias of an agent.</p>"""
    memory_id: NotRequired["aws_sdk_bedrock_agent_runtime.types.memory_id.MemoryId"]
    """<p>The unique identifier of the memory.</p>"""
    session_id: NotRequired["aws_sdk_bedrock_agent_runtime.types.session_id.SessionId"]
    """<p>The unique session identifier of the memory.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: DeleteAgentMemoryRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAgentMemoryRequest:
    out: DeleteAgentMemoryRequest = {}  # type: ignore[typeddict-item]
    return out