"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#PredictiveScalingMaxCapacityBreachBehavior``."""

from typing import Literal, TypeAlias, cast

PredictiveScalingMaxCapacityBreachBehavior: TypeAlias = Literal[
    "HonorMaxCapacity",
    "IncreaseMaxCapacity",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PredictiveScalingMaxCapacityBreachBehavior) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PredictiveScalingMaxCapacityBreachBehavior:
    return cast(PredictiveScalingMaxCapacityBreachBehavior, data)
