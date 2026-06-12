"""Generated from Smithy shape ``com.amazonaws.forecast#WhatIfForecasts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_forecast.types.what_if_forecast_summary

WhatIfForecasts: TypeAlias = list[
    "aws_sdk_forecast.types.what_if_forecast_summary.WhatIfForecastSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WhatIfForecasts) -> list:
    import aws_sdk_forecast.types.what_if_forecast_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_forecast.types.what_if_forecast_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> WhatIfForecasts:
    import aws_sdk_forecast.types.what_if_forecast_summary

    out: WhatIfForecasts = []
    for item in data:
        out.append(
            aws_sdk_forecast.types.what_if_forecast_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
