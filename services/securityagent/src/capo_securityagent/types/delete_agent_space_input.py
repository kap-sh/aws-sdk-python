"""Generated from Smithy shape ``com.amazonaws.securityagent#DeleteAgentSpaceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_securityagent.types.agent_space_id


class DeleteAgentSpaceInput(TypedDict, closed=True):
    agent_space_id: "capo_securityagent.types.agent_space_id.AgentSpaceId"
    """<p>The unique identifier of the agent space to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAgentSpaceInput) -> dict:
    out: dict = {}
    out["agentSpaceId"] = value["agent_space_id"]
    return out


def deserialize_json(data: dict) -> DeleteAgentSpaceInput:
    out: DeleteAgentSpaceInput = {}  # type: ignore[typeddict-item]
    if "agentSpaceId" in data:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        raise DeserializationError("DeleteAgentSpaceInput.agent_space_id required")
    return out
