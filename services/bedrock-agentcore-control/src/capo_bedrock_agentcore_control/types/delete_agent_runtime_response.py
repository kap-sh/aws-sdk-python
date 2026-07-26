"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DeleteAgentRuntimeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.agent_runtime_id
    import capo_bedrock_agentcore_control.types.agent_runtime_status


class DeleteAgentRuntimeResponse(TypedDict, closed=True):
    status: (
        "capo_bedrock_agentcore_control.types.agent_runtime_status.AgentRuntimeStatus"
    )
    """<p>The current status of the AgentCore Runtime deletion.</p>"""
    agent_runtime_id: NotRequired[
        "capo_bedrock_agentcore_control.types.agent_runtime_id.AgentRuntimeId"
    ]
    """<p>The unique identifier of the AgentCore Runtime.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAgentRuntimeResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.agent_runtime_status

    out["status"] = (
        capo_bedrock_agentcore_control.types.agent_runtime_status.serialize_json(
            value["status"]
        )
    )
    if "agent_runtime_id" in value:
        out["agentRuntimeId"] = value["agent_runtime_id"]
    return out


def deserialize_json(data: dict) -> DeleteAgentRuntimeResponse:
    out: DeleteAgentRuntimeResponse = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import capo_bedrock_agentcore_control.types.agent_runtime_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.agent_runtime_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("DeleteAgentRuntimeResponse.status required")
    if "agentRuntimeId" in data:
        out["agent_runtime_id"] = data["agentRuntimeId"]
    return out
