"""Generated from Smithy shape ``com.amazonaws.qconnect#CreateAIGuardrailResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.ai_guardrail_data


class CreateAIGuardrailResponse(TypedDict, closed=True):
    ai_guardrail: NotRequired["capo_qconnect.types.ai_guardrail_data.AIGuardrailData"]
    """<p>The data of the AI Guardrail.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAIGuardrailResponse) -> dict:
    out: dict = {}
    if "ai_guardrail" in value:
        import capo_qconnect.types.ai_guardrail_data

        out["aiGuardrail"] = capo_qconnect.types.ai_guardrail_data.serialize_json(
            value["ai_guardrail"]
        )
    return out


def deserialize_json(data: dict) -> CreateAIGuardrailResponse:
    out: CreateAIGuardrailResponse = {}  # type: ignore[typeddict-item]
    if "aiGuardrail" in data:
        import capo_qconnect.types.ai_guardrail_data

        out["ai_guardrail"] = capo_qconnect.types.ai_guardrail_data.deserialize_json(
            data["aiGuardrail"]
        )
    return out
