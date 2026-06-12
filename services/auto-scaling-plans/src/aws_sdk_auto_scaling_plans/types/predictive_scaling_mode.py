"""Generated from Smithy shape ``com.amazonaws.autoscalingplans#PredictiveScalingMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_auto_scaling_plans.errors import DeserializationError

PredictiveScalingMode: TypeAlias = Literal[
    "ForecastAndScale",
    "ForecastOnly",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ForecastAndScale",
        "ForecastOnly",
    )
)


def serialize_aws_json_1_1(value: PredictiveScalingMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PredictiveScalingMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PredictiveScalingMode value: {data!r}")
    return cast(PredictiveScalingMode, data)
