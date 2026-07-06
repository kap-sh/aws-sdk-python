"""Generated from Smithy shape ``com.amazonaws.qconnect#GetAIGuardrailRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.uuid_or_arn
    import aws_sdk_qconnect.types.uuid_or_arn_or_either_with_qualifier


class GetAIGuardrailRequest(TypedDict, closed=True):
    assistant_id: "aws_sdk_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    ai_guardrail_id: "aws_sdk_qconnect.types.uuid_or_arn_or_either_with_qualifier.UuidOrArnOrEitherWithQualifier"
    """<p>The identifier of the Amazon Q in Connect AI Guardrail.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAIGuardrailRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAIGuardrailRequest:
    out: GetAIGuardrailRequest = {}  # type: ignore[typeddict-item]
    return out
