"""Generated from Smithy shape ``com.amazonaws.qconnect#SpanGuardrailAssessmentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.span_guardrail_assessment

SpanGuardrailAssessmentList: TypeAlias = list[
    "aws_sdk_qconnect.types.span_guardrail_assessment.SpanGuardrailAssessment"
]


# --- restJson1 ser/de ---
def serialize_json(value: SpanGuardrailAssessmentList) -> list:
    import aws_sdk_qconnect.types.span_guardrail_assessment

    out: list = []
    for item in value:
        out.append(
            aws_sdk_qconnect.types.span_guardrail_assessment.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SpanGuardrailAssessmentList:
    import aws_sdk_qconnect.types.span_guardrail_assessment

    out: SpanGuardrailAssessmentList = []
    for item in data:
        out.append(
            aws_sdk_qconnect.types.span_guardrail_assessment.deserialize_json(item)
        )
    return out
