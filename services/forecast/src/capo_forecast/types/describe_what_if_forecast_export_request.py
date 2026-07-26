"""Generated from Smithy shape ``com.amazonaws.forecast#DescribeWhatIfForecastExportRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_forecast.errors import DeserializationError

if TYPE_CHECKING:
    import capo_forecast.types.long_arn


class DescribeWhatIfForecastExportRequest(TypedDict, closed=True):
    what_if_forecast_export_arn: "capo_forecast.types.long_arn.LongArn"
    """<p>The Amazon Resource Name (ARN) of the what-if forecast export that you are interested in.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeWhatIfForecastExportRequest) -> dict:
    out: dict = {}
    out["WhatIfForecastExportArn"] = value["what_if_forecast_export_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeWhatIfForecastExportRequest:
    out: DescribeWhatIfForecastExportRequest = {}  # type: ignore[typeddict-item]
    if "WhatIfForecastExportArn" in data:
        out["what_if_forecast_export_arn"] = data["WhatIfForecastExportArn"]
    else:
        raise DeserializationError(
            "DescribeWhatIfForecastExportRequest.what_if_forecast_export_arn required"
        )
    return out
