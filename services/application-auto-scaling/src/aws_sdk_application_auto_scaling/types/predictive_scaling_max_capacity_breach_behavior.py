"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#PredictiveScalingMaxCapacityBreachBehavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_application_auto_scaling.errors import DeserializationError

PredictiveScalingMaxCapacityBreachBehavior: TypeAlias = Literal[
    "HonorMaxCapacity",
    "IncreaseMaxCapacity",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HonorMaxCapacity",
        "IncreaseMaxCapacity",
    )
)


def serialize_aws_json_1_1(value: PredictiveScalingMaxCapacityBreachBehavior) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PredictiveScalingMaxCapacityBreachBehavior:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown PredictiveScalingMaxCapacityBreachBehavior value: {data!r}"
        )
    return cast(PredictiveScalingMaxCapacityBreachBehavior, data)
