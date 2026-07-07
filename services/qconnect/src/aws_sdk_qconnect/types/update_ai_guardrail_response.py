"""Generated from Smithy shape ``com.amazonaws.qconnect#UpdateAIGuardrailResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.ai_guardrail_data


class UpdateAIGuardrailResponse(TypedDict, closed=True):
    ai_guardrail: NotRequired[
        "aws_sdk_qconnect.types.ai_guardrail_data.AIGuardrailData"
    ]
    """<p>The data of the updated Amazon Q in Connect AI Guardrail.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAIGuardrailResponse) -> dict:
    out: dict = {}
    if "ai_guardrail" in value:
        import aws_sdk_qconnect.types.ai_guardrail_data

        out["aiGuardrail"] = aws_sdk_qconnect.types.ai_guardrail_data.serialize_json(
            value["ai_guardrail"]
        )
    return out


def deserialize_json(data: dict) -> UpdateAIGuardrailResponse:
    out: UpdateAIGuardrailResponse = {}  # type: ignore[typeddict-item]
    if "aiGuardrail" in data:
        import aws_sdk_qconnect.types.ai_guardrail_data

        out["ai_guardrail"] = aws_sdk_qconnect.types.ai_guardrail_data.deserialize_json(
            data["aiGuardrail"]
        )
    return out
