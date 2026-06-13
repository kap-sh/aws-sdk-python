"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#GuardrailAssessmentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.guardrail_assessment

GuardrailAssessmentList: TypeAlias = list[
    "aws_sdk_bedrock_agent_runtime.types.guardrail_assessment.GuardrailAssessment"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailAssessmentList) -> list:
    import aws_sdk_bedrock_agent_runtime.types.guardrail_assessment

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agent_runtime.types.guardrail_assessment.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> GuardrailAssessmentList:
    import aws_sdk_bedrock_agent_runtime.types.guardrail_assessment

    out: GuardrailAssessmentList = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agent_runtime.types.guardrail_assessment.deserialize_json(
                item
            )
        )
    return out
