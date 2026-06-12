"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyDefinitionTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_type

AutomatedReasoningPolicyDefinitionTypeList: TypeAlias = list[
    "aws_sdk_bedrock.types.automated_reasoning_policy_definition_type.AutomatedReasoningPolicyDefinitionType"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyDefinitionTypeList) -> list:
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock.types.automated_reasoning_policy_definition_type.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AutomatedReasoningPolicyDefinitionTypeList:
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_type

    out: AutomatedReasoningPolicyDefinitionTypeList = []
    for item in data:
        out.append(
            aws_sdk_bedrock.types.automated_reasoning_policy_definition_type.deserialize_json(
                item
            )
        )
    return out
