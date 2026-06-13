"""Generated from Smithy shape ``com.amazonaws.qconnect#CreateAIGuardrailResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.ai_guardrail_data


class CreateAIGuardrailResponse(TypedDict):
    ai_guardrail: NotRequired[
        "aws_sdk_qconnect.types.ai_guardrail_data.AIGuardrailData"
    ]
    """<p>The data of the AI Guardrail.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAIGuardrailResponse) -> dict:
    out: dict = {}
    if "ai_guardrail" in value:
        import aws_sdk_qconnect.types.ai_guardrail_data

        out["aiGuardrail"] = aws_sdk_qconnect.types.ai_guardrail_data.serialize_json(
            value["ai_guardrail"]
        )
    return out


def deserialize_json(data: dict) -> CreateAIGuardrailResponse:
    out: CreateAIGuardrailResponse = {}  # type: ignore[typeddict-item]
    if "aiGuardrail" in data:
        import aws_sdk_qconnect.types.ai_guardrail_data

        out["ai_guardrail"] = aws_sdk_qconnect.types.ai_guardrail_data.deserialize_json(
            data["aiGuardrail"]
        )
    return out
