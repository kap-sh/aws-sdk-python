"""Generated from Smithy shape ``com.amazonaws.connect#ContactSearchSummaryAiAgentInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.ai_agent_version_id
    import capo_connect.types.ai_use_case
    import capo_connect.types.boolean


class ContactSearchSummaryAiAgentInfo(TypedDict, closed=True):
    ai_agent_version_id: NotRequired[
        "capo_connect.types.ai_agent_version_id.AiAgentVersionId"
    ]
    """<p>The unique identifier that specifies both the AI agent ID and its version number that was involved in the contact.</p>"""
    ai_agent_escalated: NotRequired["capo_connect.types.boolean.Boolean"]
    """<p>A boolean flag indicating whether the contact initially handled by this AI agent was escalated to a human agent.</p>"""
    ai_use_case: NotRequired["capo_connect.types.ai_use_case.AiUseCase"]
    """<p>The use case or scenario for which the AI agent is involved in the contact. Valid values are <code>AgentAssistance</code> and <code>SelfService</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContactSearchSummaryAiAgentInfo) -> dict:
    out: dict = {}
    if "ai_agent_version_id" in value:
        out["AiAgentVersionId"] = value["ai_agent_version_id"]
    if "ai_agent_escalated" in value:
        out["AiAgentEscalated"] = value["ai_agent_escalated"]
    if "ai_use_case" in value:
        import capo_connect.types.ai_use_case

        out["AiUseCase"] = capo_connect.types.ai_use_case.serialize_json(
            value["ai_use_case"]
        )
    return out


def deserialize_json(data: dict) -> ContactSearchSummaryAiAgentInfo:
    out: ContactSearchSummaryAiAgentInfo = {}  # type: ignore[typeddict-item]
    if "AiAgentVersionId" in data:
        out["ai_agent_version_id"] = data["AiAgentVersionId"]
    if "AiAgentEscalated" in data:
        out["ai_agent_escalated"] = data["AiAgentEscalated"]
    if "AiUseCase" in data:
        import capo_connect.types.ai_use_case

        out["ai_use_case"] = capo_connect.types.ai_use_case.deserialize_json(
            data["AiUseCase"]
        )
    return out
