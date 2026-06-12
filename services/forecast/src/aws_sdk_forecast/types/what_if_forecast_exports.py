"""Generated from Smithy shape ``com.amazonaws.forecast#WhatIfForecastExports``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_forecast.types.what_if_forecast_export_summary

WhatIfForecastExports: TypeAlias = list[
    "aws_sdk_forecast.types.what_if_forecast_export_summary.WhatIfForecastExportSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WhatIfForecastExports) -> list:
    import aws_sdk_forecast.types.what_if_forecast_export_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_forecast.types.what_if_forecast_export_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> WhatIfForecastExports:
    import aws_sdk_forecast.types.what_if_forecast_export_summary

    out: WhatIfForecastExports = []
    for item in data:
        out.append(
            aws_sdk_forecast.types.what_if_forecast_export_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
