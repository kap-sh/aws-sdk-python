"""Generated from Smithy shape ``com.amazonaws.forecast#CreateWhatIfForecastResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_forecast.types.long_arn


class CreateWhatIfForecastResponse(TypedDict, closed=True):
    what_if_forecast_arn: NotRequired["aws_sdk_forecast.types.long_arn.LongArn"]
    """<p>The Amazon Resource Name (ARN) of the what-if forecast.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateWhatIfForecastResponse) -> dict:
    out: dict = {}
    if "what_if_forecast_arn" in value:
        out["WhatIfForecastArn"] = value["what_if_forecast_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateWhatIfForecastResponse:
    out: CreateWhatIfForecastResponse = {}  # type: ignore[typeddict-item]
    if "WhatIfForecastArn" in data:
        out["what_if_forecast_arn"] = data["WhatIfForecastArn"]
    return out
