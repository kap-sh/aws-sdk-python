"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedEvaluationCustomMetrics``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_evaluation_custom_metric_source

AutomatedEvaluationCustomMetrics: TypeAlias = list[
    "aws_sdk_bedrock.types.automated_evaluation_custom_metric_source.AutomatedEvaluationCustomMetricSource"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedEvaluationCustomMetrics) -> list:
    import aws_sdk_bedrock.types.automated_evaluation_custom_metric_source

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock.types.automated_evaluation_custom_metric_source.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AutomatedEvaluationCustomMetrics:
    import aws_sdk_bedrock.types.automated_evaluation_custom_metric_source

    out: AutomatedEvaluationCustomMetrics = []
    for item in data:
        out.append(
            aws_sdk_bedrock.types.automated_evaluation_custom_metric_source.deserialize_json(
                item
            )
        )
    return out
