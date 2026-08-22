"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#EvaluatorMetricList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.evaluator_metric

EvaluatorMetricList: TypeAlias = list[
    "capo_bedrock_agentcore.types.evaluator_metric.EvaluatorMetric"
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluatorMetricList) -> list:
    import capo_bedrock_agentcore.types.evaluator_metric

    out: list = []
    for item in value:
        out.append(capo_bedrock_agentcore.types.evaluator_metric.serialize_json(item))
    return out


def deserialize_json(data: list) -> EvaluatorMetricList:
    import capo_bedrock_agentcore.types.evaluator_metric

    out: EvaluatorMetricList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_bedrock_agentcore.types.evaluator_metric.deserialize_json(item))
    return out
