"""Generated from Smithy shape ``com.amazonaws.qconnect#AIPromptVersionSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.ai_prompt_summary
    import aws_sdk_qconnect.types.version


class AIPromptVersionSummary(TypedDict):
    ai_prompt_summary: NotRequired[
        "aws_sdk_qconnect.types.ai_prompt_summary.AIPromptSummary"
    ]
    """<p>The date for the summary of the AI Prompt version.</p>"""
    version_number: NotRequired["aws_sdk_qconnect.types.version.Version"]
    """<p>The version number for this AI Prompt version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AIPromptVersionSummary) -> dict:
    out: dict = {}
    if "ai_prompt_summary" in value:
        import aws_sdk_qconnect.types.ai_prompt_summary

        out["aiPromptSummary"] = (
            aws_sdk_qconnect.types.ai_prompt_summary.serialize_json(
                value["ai_prompt_summary"]
            )
        )
    if "version_number" in value:
        out["versionNumber"] = value["version_number"]
    return out


def deserialize_json(data: dict) -> AIPromptVersionSummary:
    out: AIPromptVersionSummary = {}  # type: ignore[typeddict-item]
    if "aiPromptSummary" in data:
        import aws_sdk_qconnect.types.ai_prompt_summary

        out["ai_prompt_summary"] = (
            aws_sdk_qconnect.types.ai_prompt_summary.deserialize_json(
                data["aiPromptSummary"]
            )
        )
    if "versionNumber" in data:
        out["version_number"] = data["versionNumber"]
    return out
