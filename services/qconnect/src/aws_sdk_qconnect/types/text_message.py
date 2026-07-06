"""Generated from Smithy shape ``com.amazonaws.qconnect#TextMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.ai_guardrail_assessment
    import aws_sdk_qconnect.types.citations
    import aws_sdk_qconnect.types.sensitive_string


class TextMessage(TypedDict, closed=True):
    value: NotRequired["aws_sdk_qconnect.types.sensitive_string.SensitiveString"]
    """<p>The value of the message data in text type.</p>"""
    citations: NotRequired["aws_sdk_qconnect.types.citations.Citations"]
    """<p>The citations associated with the text message.</p>"""
    ai_guardrail_assessment: NotRequired[
        "aws_sdk_qconnect.types.ai_guardrail_assessment.AIGuardrailAssessment"
    ]
    """<p>The AI Guardrail assessment for the text message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TextMessage) -> dict:
    out: dict = {}
    if "value" in value:
        out["value"] = value["value"]
    if "citations" in value:
        import aws_sdk_qconnect.types.citations

        out["citations"] = aws_sdk_qconnect.types.citations.serialize_json(
            value["citations"]
        )
    if "ai_guardrail_assessment" in value:
        import aws_sdk_qconnect.types.ai_guardrail_assessment

        out["aiGuardrailAssessment"] = (
            aws_sdk_qconnect.types.ai_guardrail_assessment.serialize_json(
                value["ai_guardrail_assessment"]
            )
        )
    return out


def deserialize_json(data: dict) -> TextMessage:
    out: TextMessage = {}  # type: ignore[typeddict-item]
    if "value" in data:
        out["value"] = data["value"]
    if "citations" in data:
        import aws_sdk_qconnect.types.citations

        out["citations"] = aws_sdk_qconnect.types.citations.deserialize_json(
            data["citations"]
        )
    if "aiGuardrailAssessment" in data:
        import aws_sdk_qconnect.types.ai_guardrail_assessment

        out["ai_guardrail_assessment"] = (
            aws_sdk_qconnect.types.ai_guardrail_assessment.deserialize_json(
                data["aiGuardrailAssessment"]
            )
        )
    return out
