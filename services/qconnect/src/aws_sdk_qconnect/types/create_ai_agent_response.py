"""Generated from Smithy shape ``com.amazonaws.qconnect#CreateAIAgentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.ai_agent_data


class CreateAIAgentResponse(TypedDict, closed=True):
    ai_agent: NotRequired["aws_sdk_qconnect.types.ai_agent_data.AIAgentData"]
    """<p>The data of the created AI Agent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAIAgentResponse) -> dict:
    out: dict = {}
    if "ai_agent" in value:
        import aws_sdk_qconnect.types.ai_agent_data

        out["aiAgent"] = aws_sdk_qconnect.types.ai_agent_data.serialize_json(
            value["ai_agent"]
        )
    return out


def deserialize_json(data: dict) -> CreateAIAgentResponse:
    out: CreateAIAgentResponse = {}  # type: ignore[typeddict-item]
    if "aiAgent" in data:
        import aws_sdk_qconnect.types.ai_agent_data

        out["ai_agent"] = aws_sdk_qconnect.types.ai_agent_data.deserialize_json(
            data["aiAgent"]
        )
    return out
