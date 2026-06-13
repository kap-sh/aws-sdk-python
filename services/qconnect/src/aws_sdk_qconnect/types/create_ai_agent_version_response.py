"""Generated from Smithy shape ``com.amazonaws.qconnect#CreateAIAgentVersionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.ai_agent_data
    import aws_sdk_qconnect.types.version


class CreateAIAgentVersionResponse(TypedDict):
    ai_agent: NotRequired["aws_sdk_qconnect.types.ai_agent_data.AIAgentData"]
    """<p>The data of the AI Agent version.</p>"""
    version_number: NotRequired["aws_sdk_qconnect.types.version.Version"]
    """<p>The version number of the AI Agent version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAIAgentVersionResponse) -> dict:
    out: dict = {}
    if "ai_agent" in value:
        import aws_sdk_qconnect.types.ai_agent_data

        out["aiAgent"] = aws_sdk_qconnect.types.ai_agent_data.serialize_json(
            value["ai_agent"]
        )
    if "version_number" in value:
        out["versionNumber"] = value["version_number"]
    return out


def deserialize_json(data: dict) -> CreateAIAgentVersionResponse:
    out: CreateAIAgentVersionResponse = {}  # type: ignore[typeddict-item]
    if "aiAgent" in data:
        import aws_sdk_qconnect.types.ai_agent_data

        out["ai_agent"] = aws_sdk_qconnect.types.ai_agent_data.deserialize_json(
            data["aiAgent"]
        )
    if "versionNumber" in data:
        out["version_number"] = data["versionNumber"]
    return out
