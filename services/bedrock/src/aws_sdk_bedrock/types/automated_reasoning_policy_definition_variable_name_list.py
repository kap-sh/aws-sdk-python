"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyDefinitionVariableNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_variable_name

AutomatedReasoningPolicyDefinitionVariableNameList: TypeAlias = list[
    "aws_sdk_bedrock.types.automated_reasoning_policy_definition_variable_name.AutomatedReasoningPolicyDefinitionVariableName"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyDefinitionVariableNameList) -> list:
    return list(value)


def deserialize_json(data: list) -> AutomatedReasoningPolicyDefinitionVariableNameList:
    return list(data)
