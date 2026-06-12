"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyAnnotationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_annotation

AutomatedReasoningPolicyAnnotationList: TypeAlias = list[
    "aws_sdk_bedrock.types.automated_reasoning_policy_annotation.AutomatedReasoningPolicyAnnotation"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyAnnotationList) -> list:
    import aws_sdk_bedrock.types.automated_reasoning_policy_annotation

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock.types.automated_reasoning_policy_annotation.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AutomatedReasoningPolicyAnnotationList:
    import aws_sdk_bedrock.types.automated_reasoning_policy_annotation

    out: AutomatedReasoningPolicyAnnotationList = []
    for item in data:
        out.append(
            aws_sdk_bedrock.types.automated_reasoning_policy_annotation.deserialize_json(
                item
            )
        )
    return out
