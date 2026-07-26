"""Generated from Smithy shape ``com.amazonaws.autoscalingplans#ForecastDataType``."""

from typing import Literal, TypeAlias, cast

ForecastDataType: TypeAlias = Literal[
    "CapacityForecast",
    "LoadForecast",
    "ScheduledActionMinCapacity",
    "ScheduledActionMaxCapacity",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ForecastDataType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ForecastDataType:
    return cast(ForecastDataType, data)
