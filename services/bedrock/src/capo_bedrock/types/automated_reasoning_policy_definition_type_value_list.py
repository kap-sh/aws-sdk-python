"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyDefinitionTypeValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_definition_type_value

AutomatedReasoningPolicyDefinitionTypeValueList: TypeAlias = list[
    "capo_bedrock.types.automated_reasoning_policy_definition_type_value.AutomatedReasoningPolicyDefinitionTypeValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyDefinitionTypeValueList) -> list:
    import capo_bedrock.types.automated_reasoning_policy_definition_type_value

    out: list = []
    for item in value:
        out.append(
            capo_bedrock.types.automated_reasoning_policy_definition_type_value.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AutomatedReasoningPolicyDefinitionTypeValueList:
    import capo_bedrock.types.automated_reasoning_policy_definition_type_value

    out: AutomatedReasoningPolicyDefinitionTypeValueList = []
    for item in data:
        out.append(
            capo_bedrock.types.automated_reasoning_policy_definition_type_value.deserialize_json(
                item
            )
        )
    return out
