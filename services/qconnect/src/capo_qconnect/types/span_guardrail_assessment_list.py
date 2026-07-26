"""Generated from Smithy shape ``com.amazonaws.qconnect#SpanGuardrailAssessmentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qconnect.types.span_guardrail_assessment

SpanGuardrailAssessmentList: TypeAlias = list[
    "capo_qconnect.types.span_guardrail_assessment.SpanGuardrailAssessment"
]


# --- restJson1 ser/de ---
def serialize_json(value: SpanGuardrailAssessmentList) -> list:
    import capo_qconnect.types.span_guardrail_assessment

    out: list = []
    for item in value:
        out.append(capo_qconnect.types.span_guardrail_assessment.serialize_json(item))
    return out


def deserialize_json(data: list) -> SpanGuardrailAssessmentList:
    import capo_qconnect.types.span_guardrail_assessment

    out: SpanGuardrailAssessmentList = []
    for item in data:
        out.append(capo_qconnect.types.span_guardrail_assessment.deserialize_json(item))
    return out
