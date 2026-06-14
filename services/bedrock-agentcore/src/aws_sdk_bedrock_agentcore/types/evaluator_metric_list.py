"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#EvaluatorMetricList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.evaluator_metric

EvaluatorMetricList: TypeAlias = list[
    "aws_sdk_bedrock_agentcore.types.evaluator_metric.EvaluatorMetric"
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluatorMetricList) -> list:
    import aws_sdk_bedrock_agentcore.types.evaluator_metric

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agentcore.types.evaluator_metric.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> EvaluatorMetricList:
    import aws_sdk_bedrock_agentcore.types.evaluator_metric

    out: EvaluatorMetricList = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agentcore.types.evaluator_metric.deserialize_json(item)
        )
    return out
