"""Generated from Smithy shape ``com.amazonaws.connect#AiAgentSearchCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.ai_agent_id
    import aws_sdk_connect.types.ai_agent_version_number
    import aws_sdk_connect.types.ai_use_case
    import aws_sdk_connect.types.boolean


class AiAgentSearchCriteria(TypedDict, closed=True):
    id: NotRequired["aws_sdk_connect.types.ai_agent_id.AiAgentId"]
    """<p>ID of the AI Agent that was involved in the contact.</p>"""
    version_number: NotRequired[
        "aws_sdk_connect.types.ai_agent_version_number.AiAgentVersionNumber"
    ]
    """<p>Version of the AI agent that was involved in the contact. ID is required if VersionNumber is passed.</p>"""
    ai_agent_escalated: NotRequired["aws_sdk_connect.types.boolean.Boolean"]
    """<p>A boolean flag indicating whether the contact initially handled by this AI agent was escalated to a human agent.</p>"""
    ai_use_case: NotRequired["aws_sdk_connect.types.ai_use_case.AiUseCase"]
    """<p>The use case or scenario for which the AI agent is involved in the contact.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AiAgentSearchCriteria) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "version_number" in value:
        out["VersionNumber"] = value["version_number"]
    if "ai_agent_escalated" in value:
        out["AiAgentEscalated"] = value["ai_agent_escalated"]
    if "ai_use_case" in value:
        import aws_sdk_connect.types.ai_use_case

        out["AiUseCase"] = aws_sdk_connect.types.ai_use_case.serialize_json(
            value["ai_use_case"]
        )
    return out


def deserialize_json(data: dict) -> AiAgentSearchCriteria:
    out: AiAgentSearchCriteria = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "VersionNumber" in data:
        out["version_number"] = data["VersionNumber"]
    if "AiAgentEscalated" in data:
        out["ai_agent_escalated"] = data["AiAgentEscalated"]
    if "AiUseCase" in data:
        import aws_sdk_connect.types.ai_use_case

        out["ai_use_case"] = aws_sdk_connect.types.ai_use_case.deserialize_json(
            data["AiUseCase"]
        )
    return out
