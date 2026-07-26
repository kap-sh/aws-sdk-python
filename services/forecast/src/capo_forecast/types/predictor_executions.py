"""Generated from Smithy shape ``com.amazonaws.forecast#PredictorExecutions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_forecast.types.predictor_execution

PredictorExecutions: TypeAlias = list[
    "capo_forecast.types.predictor_execution.PredictorExecution"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PredictorExecutions) -> list:
    import capo_forecast.types.predictor_execution

    out: list = []
    for item in value:
        out.append(capo_forecast.types.predictor_execution.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PredictorExecutions:
    import capo_forecast.types.predictor_execution

    out: PredictorExecutions = []
    for item in data:
        out.append(
            capo_forecast.types.predictor_execution.deserialize_aws_json_1_1(item)
        )
    return out
