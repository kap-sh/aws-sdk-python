"""Generated from Smithy shape ``com.amazonaws.forecast#Forecasts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_forecast.types.forecast_summary

Forecasts: TypeAlias = list["aws_sdk_forecast.types.forecast_summary.ForecastSummary"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Forecasts) -> list:
    import aws_sdk_forecast.types.forecast_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_forecast.types.forecast_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Forecasts:
    import aws_sdk_forecast.types.forecast_summary

    out: Forecasts = []
    for item in data:
        out.append(
            aws_sdk_forecast.types.forecast_summary.deserialize_aws_json_1_1(item)
        )
    return out
