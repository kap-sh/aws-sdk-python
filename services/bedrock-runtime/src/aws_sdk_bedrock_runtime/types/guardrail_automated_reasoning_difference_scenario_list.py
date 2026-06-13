"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailAutomatedReasoningDifferenceScenarioList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_scenario

GuardrailAutomatedReasoningDifferenceScenarioList: TypeAlias = list[
    "aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_scenario.GuardrailAutomatedReasoningScenario"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailAutomatedReasoningDifferenceScenarioList) -> list:
    import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_scenario

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_scenario.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> GuardrailAutomatedReasoningDifferenceScenarioList:
    import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_scenario

    out: GuardrailAutomatedReasoningDifferenceScenarioList = []
    for item in data:
        out.append(
            aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_scenario.deserialize_json(
                item
            )
        )
    return out
