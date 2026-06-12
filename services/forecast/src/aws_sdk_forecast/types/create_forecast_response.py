"""Generated from Smithy shape ``com.amazonaws.forecast#CreateForecastResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_forecast.types.arn


class CreateForecastResponse(TypedDict):
    forecast_arn: NotRequired["aws_sdk_forecast.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the forecast.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateForecastResponse) -> dict:
    out: dict = {}
    if "forecast_arn" in value:
        out["ForecastArn"] = value["forecast_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateForecastResponse:
    out: CreateForecastResponse = {}  # type: ignore[typeddict-item]
    if "ForecastArn" in data:
        out["forecast_arn"] = data["ForecastArn"]
    return out
