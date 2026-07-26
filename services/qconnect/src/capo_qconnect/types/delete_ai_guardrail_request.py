"""Generated from Smithy shape ``com.amazonaws.qconnect#DeleteAIGuardrailRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.uuid_or_arn
    import capo_qconnect.types.uuid_or_arn_or_either_with_qualifier


class DeleteAIGuardrailRequest(TypedDict, closed=True):
    assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    ai_guardrail_id: "capo_qconnect.types.uuid_or_arn_or_either_with_qualifier.UuidOrArnOrEitherWithQualifier"
    """<p>The identifier of the Amazon Q in Connect AI Guardrail. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAIGuardrailRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAIGuardrailRequest:
    out: DeleteAIGuardrailRequest = {}  # type: ignore[typeddict-item]
    return out
