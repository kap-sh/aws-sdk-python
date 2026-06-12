"""Generated from Smithy shape ``com.amazonaws.bedrock#EvaluationMetricNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.evaluation_metric_name

EvaluationMetricNames: TypeAlias = list[
    "aws_sdk_bedrock.types.evaluation_metric_name.EvaluationMetricName"
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationMetricNames) -> list:
    return list(value)


def deserialize_json(data: list) -> EvaluationMetricNames:
    return list(data)
