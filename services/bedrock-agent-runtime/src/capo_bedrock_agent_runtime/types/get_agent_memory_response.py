"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#GetAgentMemoryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.memories
    import capo_bedrock_agent_runtime.types.next_token


class GetAgentMemoryResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_bedrock_agent_runtime.types.next_token.NextToken"]
    """<p>If the total number of results is greater than the maxItems value provided in the request, use this token when making another request in the <code>nextToken</code> field to return the next batch of results.</p>"""
    memory_contents: NotRequired["capo_bedrock_agent_runtime.types.memories.Memories"]
    """<p>Contains details of the sessions stored in the memory</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAgentMemoryResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "memory_contents" in value:
        import capo_bedrock_agent_runtime.types.memories

        out["memoryContents"] = (
            capo_bedrock_agent_runtime.types.memories.serialize_json(
                value["memory_contents"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetAgentMemoryResponse:
    out: GetAgentMemoryResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "memoryContents" in data:
        import capo_bedrock_agent_runtime.types.memories

        out["memory_contents"] = (
            capo_bedrock_agent_runtime.types.memories.deserialize_json(
                data["memoryContents"]
            )
        )
    return out
