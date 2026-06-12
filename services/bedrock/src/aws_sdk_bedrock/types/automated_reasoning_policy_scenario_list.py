"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyScenarioList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_scenario

AutomatedReasoningPolicyScenarioList: TypeAlias = list[
    "aws_sdk_bedrock.types.automated_reasoning_policy_scenario.AutomatedReasoningPolicyScenario"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyScenarioList) -> list:
    import aws_sdk_bedrock.types.automated_reasoning_policy_scenario

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock.types.automated_reasoning_policy_scenario.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AutomatedReasoningPolicyScenarioList:
    import aws_sdk_bedrock.types.automated_reasoning_policy_scenario

    out: AutomatedReasoningPolicyScenarioList = []
    for item in data:
        out.append(
            aws_sdk_bedrock.types.automated_reasoning_policy_scenario.deserialize_json(
                item
            )
        )
    return out
