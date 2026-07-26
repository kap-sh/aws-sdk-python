"""Generated from Smithy shape ``com.amazonaws.forecast#PredictorEvaluationResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_forecast.types.evaluation_result

PredictorEvaluationResults: TypeAlias = list[
    "capo_forecast.types.evaluation_result.EvaluationResult"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PredictorEvaluationResults) -> list:
    import capo_forecast.types.evaluation_result

    out: list = []
    for item in value:
        out.append(capo_forecast.types.evaluation_result.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PredictorEvaluationResults:
    import capo_forecast.types.evaluation_result

    out: PredictorEvaluationResults = []
    for item in data:
        out.append(capo_forecast.types.evaluation_result.deserialize_aws_json_1_1(item))
    return out
