"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyTypeValueAnnotationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_type_value_annotation

AutomatedReasoningPolicyTypeValueAnnotationList: TypeAlias = list[
    "capo_bedrock.types.automated_reasoning_policy_type_value_annotation.AutomatedReasoningPolicyTypeValueAnnotation"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyTypeValueAnnotationList) -> list:
    import capo_bedrock.types.automated_reasoning_policy_type_value_annotation

    out: list = []
    for item in value:
        out.append(
            capo_bedrock.types.automated_reasoning_policy_type_value_annotation.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AutomatedReasoningPolicyTypeValueAnnotationList:
    import capo_bedrock.types.automated_reasoning_policy_type_value_annotation

    out: AutomatedReasoningPolicyTypeValueAnnotationList = []
    for item in data:
        out.append(
            capo_bedrock.types.automated_reasoning_policy_type_value_annotation.deserialize_json(
                item
            )
        )
    return out
