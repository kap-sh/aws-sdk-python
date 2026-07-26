"""Generated from Smithy shape ``com.amazonaws.connect#CreateAgentStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.agent_status_id
    import capo_connect.types.arn


class CreateAgentStatusResponse(TypedDict, closed=True):
    agent_status_arn: NotRequired["capo_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the agent status.</p>"""
    agent_status_id: NotRequired["capo_connect.types.agent_status_id.AgentStatusId"]
    """<p>The identifier of the agent status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAgentStatusResponse) -> dict:
    out: dict = {}
    if "agent_status_arn" in value:
        out["AgentStatusARN"] = value["agent_status_arn"]
    if "agent_status_id" in value:
        out["AgentStatusId"] = value["agent_status_id"]
    return out


def deserialize_json(data: dict) -> CreateAgentStatusResponse:
    out: CreateAgentStatusResponse = {}  # type: ignore[typeddict-item]
    if "AgentStatusARN" in data:
        out["agent_status_arn"] = data["AgentStatusARN"]
    if "AgentStatusId" in data:
        out["agent_status_id"] = data["AgentStatusId"]
    return out
