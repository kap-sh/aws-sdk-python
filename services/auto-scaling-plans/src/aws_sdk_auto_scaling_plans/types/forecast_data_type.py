"""Generated from Smithy shape ``com.amazonaws.autoscalingplans#ForecastDataType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_auto_scaling_plans.errors import DeserializationError

ForecastDataType: TypeAlias = Literal[
    "CapacityForecast",
    "LoadForecast",
    "ScheduledActionMinCapacity",
    "ScheduledActionMaxCapacity",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CapacityForecast",
        "LoadForecast",
        "ScheduledActionMinCapacity",
        "ScheduledActionMaxCapacity",
    )
)


def serialize_aws_json_1_1(value: ForecastDataType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ForecastDataType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ForecastDataType value: {data!r}")
    return cast(ForecastDataType, data)
