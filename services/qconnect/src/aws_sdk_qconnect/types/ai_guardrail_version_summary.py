"""Generated from Smithy shape ``com.amazonaws.qconnect#AIGuardrailVersionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.ai_guardrail_summary
    import aws_sdk_qconnect.types.version


class AIGuardrailVersionSummary(TypedDict, closed=True):
    ai_guardrail_summary: NotRequired[
        "aws_sdk_qconnect.types.ai_guardrail_summary.AIGuardrailSummary"
    ]
    """<p>The data for the summary of the AI Guardrail version.</p>"""
    version_number: NotRequired["aws_sdk_qconnect.types.version.Version"]
    """<p>The version number for this AI Guardrail version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AIGuardrailVersionSummary) -> dict:
    out: dict = {}
    if "ai_guardrail_summary" in value:
        import aws_sdk_qconnect.types.ai_guardrail_summary

        out["aiGuardrailSummary"] = (
            aws_sdk_qconnect.types.ai_guardrail_summary.serialize_json(
                value["ai_guardrail_summary"]
            )
        )
    if "version_number" in value:
        out["versionNumber"] = value["version_number"]
    return out


def deserialize_json(data: dict) -> AIGuardrailVersionSummary:
    out: AIGuardrailVersionSummary = {}  # type: ignore[typeddict-item]
    if "aiGuardrailSummary" in data:
        import aws_sdk_qconnect.types.ai_guardrail_summary

        out["ai_guardrail_summary"] = (
            aws_sdk_qconnect.types.ai_guardrail_summary.deserialize_json(
                data["aiGuardrailSummary"]
            )
        )
    if "versionNumber" in data:
        out["version_number"] = data["versionNumber"]
    return out
