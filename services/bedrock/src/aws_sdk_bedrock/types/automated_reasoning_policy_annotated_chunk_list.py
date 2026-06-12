"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyAnnotatedChunkList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_annotated_chunk

AutomatedReasoningPolicyAnnotatedChunkList: TypeAlias = list[
    "aws_sdk_bedrock.types.automated_reasoning_policy_annotated_chunk.AutomatedReasoningPolicyAnnotatedChunk"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyAnnotatedChunkList) -> list:
    import aws_sdk_bedrock.types.automated_reasoning_policy_annotated_chunk

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock.types.automated_reasoning_policy_annotated_chunk.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AutomatedReasoningPolicyAnnotatedChunkList:
    import aws_sdk_bedrock.types.automated_reasoning_policy_annotated_chunk

    out: AutomatedReasoningPolicyAnnotatedChunkList = []
    for item in data:
        out.append(
            aws_sdk_bedrock.types.automated_reasoning_policy_annotated_chunk.deserialize_json(
                item
            )
        )
    return out
