"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyTypeValueAnnotationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_type_value_annotation

AutomatedReasoningPolicyTypeValueAnnotationList: TypeAlias = list[
    "aws_sdk_bedrock.types.automated_reasoning_policy_type_value_annotation.AutomatedReasoningPolicyTypeValueAnnotation"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyTypeValueAnnotationList) -> list:
    import aws_sdk_bedrock.types.automated_reasoning_policy_type_value_annotation

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock.types.automated_reasoning_policy_type_value_annotation.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AutomatedReasoningPolicyTypeValueAnnotationList:
    import aws_sdk_bedrock.types.automated_reasoning_policy_type_value_annotation

    out: AutomatedReasoningPolicyTypeValueAnnotationList = []
    for item in data:
        out.append(
            aws_sdk_bedrock.types.automated_reasoning_policy_type_value_annotation.deserialize_json(
                item
            )
        )
    return out
