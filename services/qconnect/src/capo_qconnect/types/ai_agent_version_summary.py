"""Generated from Smithy shape ``com.amazonaws.qconnect#AIAgentVersionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.ai_agent_summary
    import capo_qconnect.types.version


class AIAgentVersionSummary(TypedDict, closed=True):
    ai_agent_summary: NotRequired["capo_qconnect.types.ai_agent_summary.AIAgentSummary"]
    """<p>The data for the summary of the AI Agent version.</p>"""
    version_number: NotRequired["capo_qconnect.types.version.Version"]
    """<p>The version number for this AI Agent version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AIAgentVersionSummary) -> dict:
    out: dict = {}
    if "ai_agent_summary" in value:
        import capo_qconnect.types.ai_agent_summary

        out["aiAgentSummary"] = capo_qconnect.types.ai_agent_summary.serialize_json(
            value["ai_agent_summary"]
        )
    if "version_number" in value:
        out["versionNumber"] = value["version_number"]
    return out


def deserialize_json(data: dict) -> AIAgentVersionSummary:
    out: AIAgentVersionSummary = {}  # type: ignore[typeddict-item]
    if "aiAgentSummary" in data:
        import capo_qconnect.types.ai_agent_summary

        out["ai_agent_summary"] = capo_qconnect.types.ai_agent_summary.deserialize_json(
            data["aiAgentSummary"]
        )
    if "versionNumber" in data:
        out["version_number"] = data["versionNumber"]
    return out
