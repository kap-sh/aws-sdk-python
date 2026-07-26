"""Generated from Smithy shape ``com.amazonaws.bedrock#HumanEvaluationCustomMetrics``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.human_evaluation_custom_metric

HumanEvaluationCustomMetrics: TypeAlias = list[
    "capo_bedrock.types.human_evaluation_custom_metric.HumanEvaluationCustomMetric"
]


# --- restJson1 ser/de ---
def serialize_json(value: HumanEvaluationCustomMetrics) -> list:
    import capo_bedrock.types.human_evaluation_custom_metric

    out: list = []
    for item in value:
        out.append(
            capo_bedrock.types.human_evaluation_custom_metric.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> HumanEvaluationCustomMetrics:
    import capo_bedrock.types.human_evaluation_custom_metric

    out: HumanEvaluationCustomMetrics = []
    for item in data:
        out.append(
            capo_bedrock.types.human_evaluation_custom_metric.deserialize_json(item)
        )
    return out
