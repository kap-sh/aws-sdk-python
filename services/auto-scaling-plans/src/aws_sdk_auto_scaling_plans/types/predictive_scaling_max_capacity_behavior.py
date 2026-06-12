"""Generated from Smithy shape ``com.amazonaws.autoscalingplans#PredictiveScalingMaxCapacityBehavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_auto_scaling_plans.errors import DeserializationError

PredictiveScalingMaxCapacityBehavior: TypeAlias = Literal[
    "SetForecastCapacityToMaxCapacity",
    "SetMaxCapacityToForecastCapacity",
    "SetMaxCapacityAboveForecastCapacity",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SetForecastCapacityToMaxCapacity",
        "SetMaxCapacityToForecastCapacity",
        "SetMaxCapacityAboveForecastCapacity",
    )
)


def serialize_aws_json_1_1(value: PredictiveScalingMaxCapacityBehavior) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PredictiveScalingMaxCapacityBehavior:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown PredictiveScalingMaxCapacityBehavior value: {data!r}"
        )
    return cast(PredictiveScalingMaxCapacityBehavior, data)
