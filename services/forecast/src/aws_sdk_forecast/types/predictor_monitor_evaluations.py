"""Generated from Smithy shape ``com.amazonaws.forecast#PredictorMonitorEvaluations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_forecast.types.predictor_monitor_evaluation

PredictorMonitorEvaluations: TypeAlias = list[
    "aws_sdk_forecast.types.predictor_monitor_evaluation.PredictorMonitorEvaluation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PredictorMonitorEvaluations) -> list:
    import aws_sdk_forecast.types.predictor_monitor_evaluation

    out: list = []
    for item in value:
        out.append(
            aws_sdk_forecast.types.predictor_monitor_evaluation.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PredictorMonitorEvaluations:
    import aws_sdk_forecast.types.predictor_monitor_evaluation

    out: PredictorMonitorEvaluations = []
    for item in data:
        out.append(
            aws_sdk_forecast.types.predictor_monitor_evaluation.deserialize_aws_json_1_1(
                item
            )
        )
    return out
