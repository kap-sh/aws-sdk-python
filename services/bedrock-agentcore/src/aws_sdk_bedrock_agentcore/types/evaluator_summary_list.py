"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#EvaluatorSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.evaluator_summary

EvaluatorSummaryList: TypeAlias = list["aws_sdk_bedrock_agentcore.types.evaluator_summary.EvaluatorSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluatorSummaryList) -> list:
    import aws_sdk_bedrock_agentcore.types.evaluator_summary
    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock_agentcore.types.evaluator_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> EvaluatorSummaryList:
    import aws_sdk_bedrock_agentcore.types.evaluator_summary
    out: EvaluatorSummaryList = []
    for item in data:
        out.append(aws_sdk_bedrock_agentcore.types.evaluator_summary.deserialize_json(item))
    return out