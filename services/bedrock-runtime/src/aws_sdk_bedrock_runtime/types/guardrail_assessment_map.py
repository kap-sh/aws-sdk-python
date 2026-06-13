"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailAssessmentMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.guardrail_assessment

GuardrailAssessmentMap: TypeAlias = dict[
    "str", "aws_sdk_bedrock_runtime.types.guardrail_assessment.GuardrailAssessment"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: GuardrailAssessmentMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_bedrock_runtime.types.guardrail_assessment

        out[key] = aws_sdk_bedrock_runtime.types.guardrail_assessment.serialize_json(
            value
        )
    return out


def deserialize_json(data: dict) -> GuardrailAssessmentMap:
    out: GuardrailAssessmentMap = {}
    for key, value in data.items():
        import aws_sdk_bedrock_runtime.types.guardrail_assessment

        out[key] = aws_sdk_bedrock_runtime.types.guardrail_assessment.deserialize_json(
            value
        )
    return out
