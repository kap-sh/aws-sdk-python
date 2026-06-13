"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#BatchEvaluationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.batch_evaluation_summary

BatchEvaluationSummaryList: TypeAlias = list["aws_sdk_bedrock_agentcore.types.batch_evaluation_summary.BatchEvaluationSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: BatchEvaluationSummaryList) -> list:
    import aws_sdk_bedrock_agentcore.types.batch_evaluation_summary
    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock_agentcore.types.batch_evaluation_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> BatchEvaluationSummaryList:
    import aws_sdk_bedrock_agentcore.types.batch_evaluation_summary
    out: BatchEvaluationSummaryList = []
    for item in data:
        out.append(aws_sdk_bedrock_agentcore.types.batch_evaluation_summary.deserialize_json(item))
    return out