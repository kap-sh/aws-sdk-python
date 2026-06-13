"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailAutomatedReasoningFindingList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_finding

GuardrailAutomatedReasoningFindingList: TypeAlias = list[
    "aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_finding.GuardrailAutomatedReasoningFinding"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailAutomatedReasoningFindingList) -> list:
    import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_finding

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_finding.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> GuardrailAutomatedReasoningFindingList:
    import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_finding

    out: GuardrailAutomatedReasoningFindingList = []
    for item in data:
        out.append(
            aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_finding.deserialize_json(
                item
            )
        )
    return out
