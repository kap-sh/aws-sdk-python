"""Generated from Smithy shape ``com.amazonaws.qconnect#GetAIPromptResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.ai_prompt_data
    import aws_sdk_qconnect.types.version


class GetAIPromptResponse(TypedDict):
    ai_prompt: NotRequired["aws_sdk_qconnect.types.ai_prompt_data.AIPromptData"]
    """<p>The data of the AI Prompt.</p>"""
    version_number: NotRequired["aws_sdk_qconnect.types.version.Version"]
    """<p>The version number of the AI Prompt version (returned if an AI Prompt version was specified via use of a qualifier for the <code>aiPromptId</code> on the request). </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAIPromptResponse) -> dict:
    out: dict = {}
    if "ai_prompt" in value:
        import aws_sdk_qconnect.types.ai_prompt_data

        out["aiPrompt"] = aws_sdk_qconnect.types.ai_prompt_data.serialize_json(
            value["ai_prompt"]
        )
    if "version_number" in value:
        out["versionNumber"] = value["version_number"]
    return out


def deserialize_json(data: dict) -> GetAIPromptResponse:
    out: GetAIPromptResponse = {}  # type: ignore[typeddict-item]
    if "aiPrompt" in data:
        import aws_sdk_qconnect.types.ai_prompt_data

        out["ai_prompt"] = aws_sdk_qconnect.types.ai_prompt_data.deserialize_json(
            data["aiPrompt"]
        )
    if "versionNumber" in data:
        out["version_number"] = data["versionNumber"]
    return out
