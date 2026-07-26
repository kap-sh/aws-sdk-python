"""Generated from Smithy shape ``com.amazonaws.qconnect#AIPromptVersionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.ai_prompt_summary
    import capo_qconnect.types.version


class AIPromptVersionSummary(TypedDict, closed=True):
    ai_prompt_summary: NotRequired[
        "capo_qconnect.types.ai_prompt_summary.AIPromptSummary"
    ]
    """<p>The date for the summary of the AI Prompt version.</p>"""
    version_number: NotRequired["capo_qconnect.types.version.Version"]
    """<p>The version number for this AI Prompt version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AIPromptVersionSummary) -> dict:
    out: dict = {}
    if "ai_prompt_summary" in value:
        import capo_qconnect.types.ai_prompt_summary

        out["aiPromptSummary"] = capo_qconnect.types.ai_prompt_summary.serialize_json(
            value["ai_prompt_summary"]
        )
    if "version_number" in value:
        out["versionNumber"] = value["version_number"]
    return out


def deserialize_json(data: dict) -> AIPromptVersionSummary:
    out: AIPromptVersionSummary = {}  # type: ignore[typeddict-item]
    if "aiPromptSummary" in data:
        import capo_qconnect.types.ai_prompt_summary

        out["ai_prompt_summary"] = (
            capo_qconnect.types.ai_prompt_summary.deserialize_json(
                data["aiPromptSummary"]
            )
        )
    if "versionNumber" in data:
        out["version_number"] = data["versionNumber"]
    return out
