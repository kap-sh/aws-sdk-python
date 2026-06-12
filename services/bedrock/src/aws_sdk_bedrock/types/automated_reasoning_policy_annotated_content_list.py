"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyAnnotatedContentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_annotated_content

AutomatedReasoningPolicyAnnotatedContentList: TypeAlias = list[
    "aws_sdk_bedrock.types.automated_reasoning_policy_annotated_content.AutomatedReasoningPolicyAnnotatedContent"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyAnnotatedContentList) -> list:
    import aws_sdk_bedrock.types.automated_reasoning_policy_annotated_content

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock.types.automated_reasoning_policy_annotated_content.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AutomatedReasoningPolicyAnnotatedContentList:
    import aws_sdk_bedrock.types.automated_reasoning_policy_annotated_content

    out: AutomatedReasoningPolicyAnnotatedContentList = []
    for item in data:
        out.append(
            aws_sdk_bedrock.types.automated_reasoning_policy_annotated_content.deserialize_json(
                item
            )
        )
    return out
