"""Generated from Smithy shape ``com.amazonaws.groundstation#RegisterAgentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.uuid


class RegisterAgentResponse(TypedDict, closed=True):
    agent_id: NotRequired["aws_sdk_groundstation.types.uuid.Uuid"]
    """<p>UUID of registered agent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterAgentResponse) -> dict:
    out: dict = {}
    if "agent_id" in value:
        out["agentId"] = value["agent_id"]
    return out


def deserialize_json(data: dict) -> RegisterAgentResponse:
    out: RegisterAgentResponse = {}  # type: ignore[typeddict-item]
    if "agentId" in data:
        out["agent_id"] = data["agentId"]
    return out
