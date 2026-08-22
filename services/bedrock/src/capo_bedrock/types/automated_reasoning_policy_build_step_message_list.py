"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyBuildStepMessageList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_build_step_message

AutomatedReasoningPolicyBuildStepMessageList: TypeAlias = list[
    "capo_bedrock.types.automated_reasoning_policy_build_step_message.AutomatedReasoningPolicyBuildStepMessage"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyBuildStepMessageList) -> list:
    import capo_bedrock.types.automated_reasoning_policy_build_step_message

    out: list = []
    for item in value:
        out.append(
            capo_bedrock.types.automated_reasoning_policy_build_step_message.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AutomatedReasoningPolicyBuildStepMessageList:
    import capo_bedrock.types.automated_reasoning_policy_build_step_message

    out: AutomatedReasoningPolicyBuildStepMessageList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock.types.automated_reasoning_policy_build_step_message.deserialize_json(
                item
            )
        )
    return out
