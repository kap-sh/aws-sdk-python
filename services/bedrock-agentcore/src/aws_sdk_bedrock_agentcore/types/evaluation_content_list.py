"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#EvaluationContentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.evaluation_content

EvaluationContentList: TypeAlias = list[
    "aws_sdk_bedrock_agentcore.types.evaluation_content.EvaluationContent"
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationContentList) -> list:
    import aws_sdk_bedrock_agentcore.types.evaluation_content

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agentcore.types.evaluation_content.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> EvaluationContentList:
    import aws_sdk_bedrock_agentcore.types.evaluation_content

    out: EvaluationContentList = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agentcore.types.evaluation_content.deserialize_json(item)
        )
    return out
