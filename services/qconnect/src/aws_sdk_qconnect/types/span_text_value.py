"""Generated from Smithy shape ``com.amazonaws.qconnect#SpanTextValue``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.ai_guardrail_assessment
    import aws_sdk_qconnect.types.non_empty_sensitive_string
    import aws_sdk_qconnect.types.span_citation_list


class SpanTextValue(TypedDict):
    value: "aws_sdk_qconnect.types.non_empty_sensitive_string.NonEmptySensitiveString"
    """<p>String content of the message text</p>"""
    citations: NotRequired["aws_sdk_qconnect.types.span_citation_list.SpanCitationList"]
    """<p>The citations associated with the span text.</p>"""
    ai_guardrail_assessment: NotRequired[
        "aws_sdk_qconnect.types.ai_guardrail_assessment.AIGuardrailAssessment"
    ]
    """<p>The AI Guardrail assessment for the span text.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SpanTextValue) -> dict:
    out: dict = {}
    out["value"] = value["value"]
    if "citations" in value:
        import aws_sdk_qconnect.types.span_citation_list

        out["citations"] = aws_sdk_qconnect.types.span_citation_list.serialize_json(
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


def deserialize_json(data: dict) -> SpanTextValue:
    out: SpanTextValue = {}  # type: ignore[typeddict-item]
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("SpanTextValue.value required")
    if "citations" in data:
        import aws_sdk_qconnect.types.span_citation_list

        out["citations"] = aws_sdk_qconnect.types.span_citation_list.deserialize_json(
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
