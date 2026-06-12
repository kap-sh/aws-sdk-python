"""Generated from Smithy shape ``com.amazonaws.forecast#DeleteForecastRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_forecast.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_forecast.types.arn


class DeleteForecastRequest(TypedDict):
    forecast_arn: "aws_sdk_forecast.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the forecast to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteForecastRequest) -> dict:
    out: dict = {}
    out["ForecastArn"] = value["forecast_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteForecastRequest:
    out: DeleteForecastRequest = {}  # type: ignore[typeddict-item]
    if "ForecastArn" in data:
        out["forecast_arn"] = data["ForecastArn"]
    else:
        raise DeserializationError("DeleteForecastRequest.forecast_arn required")
    return out
