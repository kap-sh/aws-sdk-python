"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#EvaluationResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.evaluation_result_content

EvaluationResults: TypeAlias = list[
    "aws_sdk_bedrock_agentcore.types.evaluation_result_content.EvaluationResultContent"
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationResults) -> list:
    import aws_sdk_bedrock_agentcore.types.evaluation_result_content

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agentcore.types.evaluation_result_content.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> EvaluationResults:
    import aws_sdk_bedrock_agentcore.types.evaluation_result_content

    out: EvaluationResults = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agentcore.types.evaluation_result_content.deserialize_json(
                item
            )
        )
    return out
