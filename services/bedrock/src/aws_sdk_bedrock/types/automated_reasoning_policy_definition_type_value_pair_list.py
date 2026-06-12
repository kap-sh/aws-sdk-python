"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyDefinitionTypeValuePairList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_type_value_pair

AutomatedReasoningPolicyDefinitionTypeValuePairList: TypeAlias = list[
    "aws_sdk_bedrock.types.automated_reasoning_policy_definition_type_value_pair.AutomatedReasoningPolicyDefinitionTypeValuePair"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyDefinitionTypeValuePairList) -> list:
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_type_value_pair

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock.types.automated_reasoning_policy_definition_type_value_pair.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AutomatedReasoningPolicyDefinitionTypeValuePairList:
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_type_value_pair

    out: AutomatedReasoningPolicyDefinitionTypeValuePairList = []
    for item in data:
        out.append(
            aws_sdk_bedrock.types.automated_reasoning_policy_definition_type_value_pair.deserialize_json(
                item
            )
        )
    return out
