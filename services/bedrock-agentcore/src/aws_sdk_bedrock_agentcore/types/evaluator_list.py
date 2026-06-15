"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#EvaluatorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.evaluator

EvaluatorList: TypeAlias = list["aws_sdk_bedrock_agentcore.types.evaluator.Evaluator"]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluatorList) -> list:
    import aws_sdk_bedrock_agentcore.types.evaluator

    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock_agentcore.types.evaluator.serialize_json(item))
    return out


def deserialize_json(data: list) -> EvaluatorList:
    import aws_sdk_bedrock_agentcore.types.evaluator

    out: EvaluatorList = []
    for item in data:
        out.append(aws_sdk_bedrock_agentcore.types.evaluator.deserialize_json(item))
    return out
