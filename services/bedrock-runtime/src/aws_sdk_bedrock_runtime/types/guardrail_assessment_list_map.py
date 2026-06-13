"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailAssessmentListMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.guardrail_assessment_list

GuardrailAssessmentListMap: TypeAlias = dict[
    "str",
    "aws_sdk_bedrock_runtime.types.guardrail_assessment_list.GuardrailAssessmentList",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: GuardrailAssessmentListMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_bedrock_runtime.types.guardrail_assessment_list

        out[key] = (
            aws_sdk_bedrock_runtime.types.guardrail_assessment_list.serialize_json(
                value
            )
        )
    return out


def deserialize_json(data: dict) -> GuardrailAssessmentListMap:
    out: GuardrailAssessmentListMap = {}
    for key, value in data.items():
        import aws_sdk_bedrock_runtime.types.guardrail_assessment_list

        out[key] = (
            aws_sdk_bedrock_runtime.types.guardrail_assessment_list.deserialize_json(
                value
            )
        )
    return out
