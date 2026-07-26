"""Generated from Smithy shape ``com.amazonaws.qconnect#UpdateAIAgentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.ai_agent_data


class UpdateAIAgentResponse(TypedDict, closed=True):
    ai_agent: NotRequired["capo_qconnect.types.ai_agent_data.AIAgentData"]
    """<p>The data of the updated Amazon Q in Connect AI Agent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAIAgentResponse) -> dict:
    out: dict = {}
    if "ai_agent" in value:
        import capo_qconnect.types.ai_agent_data

        out["aiAgent"] = capo_qconnect.types.ai_agent_data.serialize_json(
            value["ai_agent"]
        )
    return out


def deserialize_json(data: dict) -> UpdateAIAgentResponse:
    out: UpdateAIAgentResponse = {}  # type: ignore[typeddict-item]
    if "aiAgent" in data:
        import capo_qconnect.types.ai_agent_data

        out["ai_agent"] = capo_qconnect.types.ai_agent_data.deserialize_json(
            data["aiAgent"]
        )
    return out
