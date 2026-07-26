"""Generated from Smithy shape ``com.amazonaws.qconnect#CreateAIGuardrailVersionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.ai_guardrail_data
    import capo_qconnect.types.version


class CreateAIGuardrailVersionResponse(TypedDict, closed=True):
    ai_guardrail: NotRequired["capo_qconnect.types.ai_guardrail_data.AIGuardrailData"]
    """<p>The data of the AI Guardrail version.</p>"""
    version_number: NotRequired["capo_qconnect.types.version.Version"]
    """<p>The version number of the AI Guardrail version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAIGuardrailVersionResponse) -> dict:
    out: dict = {}
    if "ai_guardrail" in value:
        import capo_qconnect.types.ai_guardrail_data

        out["aiGuardrail"] = capo_qconnect.types.ai_guardrail_data.serialize_json(
            value["ai_guardrail"]
        )
    if "version_number" in value:
        out["versionNumber"] = value["version_number"]
    return out


def deserialize_json(data: dict) -> CreateAIGuardrailVersionResponse:
    out: CreateAIGuardrailVersionResponse = {}  # type: ignore[typeddict-item]
    if "aiGuardrail" in data:
        import capo_qconnect.types.ai_guardrail_data

        out["ai_guardrail"] = capo_qconnect.types.ai_guardrail_data.deserialize_json(
            data["aiGuardrail"]
        )
    if "versionNumber" in data:
        out["version_number"] = data["versionNumber"]
    return out
