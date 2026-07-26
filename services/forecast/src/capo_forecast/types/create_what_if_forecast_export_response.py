"""Generated from Smithy shape ``com.amazonaws.forecast#CreateWhatIfForecastExportResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_forecast.types.long_arn


class CreateWhatIfForecastExportResponse(TypedDict, closed=True):
    what_if_forecast_export_arn: NotRequired["capo_forecast.types.long_arn.LongArn"]
    """<p>The Amazon Resource Name (ARN) of the what-if forecast.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateWhatIfForecastExportResponse) -> dict:
    out: dict = {}
    if "what_if_forecast_export_arn" in value:
        out["WhatIfForecastExportArn"] = value["what_if_forecast_export_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateWhatIfForecastExportResponse:
    out: CreateWhatIfForecastExportResponse = {}  # type: ignore[typeddict-item]
    if "WhatIfForecastExportArn" in data:
        out["what_if_forecast_export_arn"] = data["WhatIfForecastExportArn"]
    return out
