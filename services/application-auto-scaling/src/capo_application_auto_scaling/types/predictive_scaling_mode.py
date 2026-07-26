"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#PredictiveScalingMode``."""

from typing import Literal, TypeAlias, cast

PredictiveScalingMode: TypeAlias = Literal[
    "ForecastOnly",
    "ForecastAndScale",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PredictiveScalingMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PredictiveScalingMode:
    return cast(PredictiveScalingMode, data)
