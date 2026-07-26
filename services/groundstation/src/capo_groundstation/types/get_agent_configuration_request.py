"""Generated from Smithy shape ``com.amazonaws.groundstation#GetAgentConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_groundstation.types.uuid


class GetAgentConfigurationRequest(TypedDict, closed=True):
    agent_id: "capo_groundstation.types.uuid.Uuid"
    """<p>UUID of agent to get configuration information for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAgentConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAgentConfigurationRequest:
    out: GetAgentConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
