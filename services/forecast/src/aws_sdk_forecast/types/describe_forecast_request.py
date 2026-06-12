"""Generated from Smithy shape ``com.amazonaws.forecast#DescribeForecastRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_forecast.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_forecast.types.arn


class DescribeForecastRequest(TypedDict):
    forecast_arn: "aws_sdk_forecast.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the forecast.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeForecastRequest) -> dict:
    out: dict = {}
    out["ForecastArn"] = value["forecast_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeForecastRequest:
    out: DescribeForecastRequest = {}  # type: ignore[typeddict-item]
    if "ForecastArn" in data:
        out["forecast_arn"] = data["ForecastArn"]
    else:
        raise DeserializationError("DescribeForecastRequest.forecast_arn required")
    return out
