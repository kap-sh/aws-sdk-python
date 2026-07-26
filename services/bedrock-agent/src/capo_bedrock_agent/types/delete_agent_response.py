"""Generated from Smithy shape ``com.amazonaws.bedrockagent#DeleteAgentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.agent_status
    import capo_bedrock_agent.types.id


class DeleteAgentResponse(TypedDict, closed=True):
    agent_id: "capo_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the agent that was deleted.</p>"""
    agent_status: "capo_bedrock_agent.types.agent_status.AgentStatus"
    """<p>The status of the agent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAgentResponse) -> dict:
    out: dict = {}
    out["agentId"] = value["agent_id"]
    import capo_bedrock_agent.types.agent_status

    out["agentStatus"] = capo_bedrock_agent.types.agent_status.serialize_json(
        value["agent_status"]
    )
    return out


def deserialize_json(data: dict) -> DeleteAgentResponse:
    out: DeleteAgentResponse = {}  # type: ignore[typeddict-item]
    if "agentId" in data:
        out["agent_id"] = data["agentId"]
    else:
        raise DeserializationError("DeleteAgentResponse.agent_id required")
    if "agentStatus" in data:
        import capo_bedrock_agent.types.agent_status

        out["agent_status"] = capo_bedrock_agent.types.agent_status.deserialize_json(
            data["agentStatus"]
        )
    else:
        raise DeserializationError("DeleteAgentResponse.agent_status required")
    return out
