"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyDefinitionVariableList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_variable

AutomatedReasoningPolicyDefinitionVariableList: TypeAlias = list[
    "aws_sdk_bedrock.types.automated_reasoning_policy_definition_variable.AutomatedReasoningPolicyDefinitionVariable"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyDefinitionVariableList) -> list:
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_variable

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock.types.automated_reasoning_policy_definition_variable.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AutomatedReasoningPolicyDefinitionVariableList:
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_variable

    out: AutomatedReasoningPolicyDefinitionVariableList = []
    for item in data:
        out.append(
            aws_sdk_bedrock.types.automated_reasoning_policy_definition_variable.deserialize_json(
                item
            )
        )
    return out
