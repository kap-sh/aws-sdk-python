"""Generated from Smithy shape ``com.amazonaws.autoscalingplans#PredictiveScalingMaxCapacityBehavior``."""

from typing import Literal, TypeAlias, cast

PredictiveScalingMaxCapacityBehavior: TypeAlias = Literal[
    "SetForecastCapacityToMaxCapacity",
    "SetMaxCapacityToForecastCapacity",
    "SetMaxCapacityAboveForecastCapacity",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PredictiveScalingMaxCapacityBehavior) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PredictiveScalingMaxCapacityBehavior:
    return cast(PredictiveScalingMaxCapacityBehavior, data)
