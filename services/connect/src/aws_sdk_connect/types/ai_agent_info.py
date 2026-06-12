"""Generated from Smithy shape ``com.amazonaws.connect#AiAgentInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.ai_agent_version_id
    import aws_sdk_connect.types.ai_use_case
    import aws_sdk_connect.types.boolean


class AiAgentInfo(TypedDict):
    ai_use_case: NotRequired["aws_sdk_connect.types.ai_use_case.AiUseCase"]
    """<p> The use case or scenario for which the AI agent is involved in the contact </p>"""
    ai_agent_version_id: NotRequired[
        "aws_sdk_connect.types.ai_agent_version_id.AiAgentVersionId"
    ]
    """<p> The unique identifier that specifies both the AI agent ID and its version number that was involved in the contact </p>"""
    ai_agent_escalated: "aws_sdk_connect.types.boolean.Boolean"
    """<p> A boolean flag indicating whether the contact initially handled by this AI agent was escalated to a human agent. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AiAgentInfo) -> dict:
    out: dict = {}
    if "ai_use_case" in value:
        import aws_sdk_connect.types.ai_use_case

        out["AiUseCase"] = aws_sdk_connect.types.ai_use_case.serialize_json(
            value["ai_use_case"]
        )
    if "ai_agent_version_id" in value:
        out["AiAgentVersionId"] = value["ai_agent_version_id"]
    out["AiAgentEscalated"] = value.get("ai_agent_escalated", False)
    return out


def deserialize_json(data: dict) -> AiAgentInfo:
    out: AiAgentInfo = {}  # type: ignore[typeddict-item]
    if "AiUseCase" in data:
        import aws_sdk_connect.types.ai_use_case

        out["ai_use_case"] = aws_sdk_connect.types.ai_use_case.deserialize_json(
            data["AiUseCase"]
        )
    if "AiAgentVersionId" in data:
        out["ai_agent_version_id"] = data["AiAgentVersionId"]
    if "AiAgentEscalated" in data:
        out["ai_agent_escalated"] = data["AiAgentEscalated"]
    else:
        out["ai_agent_escalated"] = False
    return out
