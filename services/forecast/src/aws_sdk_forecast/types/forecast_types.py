"""Generated from Smithy shape ``com.amazonaws.forecast#ForecastTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_forecast.types.forecast_type

ForecastTypes: TypeAlias = list["aws_sdk_forecast.types.forecast_type.ForecastType"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ForecastTypes) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ForecastTypes:
    return list(data)
