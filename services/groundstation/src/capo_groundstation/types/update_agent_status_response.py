"""Generated from Smithy shape ``com.amazonaws.groundstation#UpdateAgentStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_groundstation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_groundstation.types.uuid


class UpdateAgentStatusResponse(TypedDict, closed=True):
    agent_id: "capo_groundstation.types.uuid.Uuid"
    """<p>UUID of updated agent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAgentStatusResponse) -> dict:
    out: dict = {}
    out["agentId"] = value["agent_id"]
    return out


def deserialize_json(data: dict) -> UpdateAgentStatusResponse:
    out: UpdateAgentStatusResponse = {}  # type: ignore[typeddict-item]
    if "agentId" in data:
        out["agent_id"] = data["agentId"]
    else:
        raise DeserializationError("UpdateAgentStatusResponse.agent_id required")
    return out
