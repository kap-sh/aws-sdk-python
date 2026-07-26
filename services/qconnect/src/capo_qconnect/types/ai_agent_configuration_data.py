"""Generated from Smithy shape ``com.amazonaws.qconnect#AIAgentConfigurationData``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qconnect.types.uuid_with_qualifier


class AIAgentConfigurationData(TypedDict, closed=True):
    ai_agent_id: "capo_qconnect.types.uuid_with_qualifier.UuidWithQualifier"
    """<p>The ID of the AI Agent to be configured.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AIAgentConfigurationData) -> dict:
    out: dict = {}
    out["aiAgentId"] = value["ai_agent_id"]
    return out


def deserialize_json(data: dict) -> AIAgentConfigurationData:
    out: AIAgentConfigurationData = {}  # type: ignore[typeddict-item]
    if "aiAgentId" in data:
        out["ai_agent_id"] = data["aiAgentId"]
    else:
        raise DeserializationError("AIAgentConfigurationData.ai_agent_id required")
    return out
