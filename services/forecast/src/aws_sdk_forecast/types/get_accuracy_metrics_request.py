"""Generated from Smithy shape ``com.amazonaws.forecast#GetAccuracyMetricsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_forecast.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_forecast.types.arn


class GetAccuracyMetricsRequest(TypedDict):
    predictor_arn: "aws_sdk_forecast.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the predictor to get metrics for.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAccuracyMetricsRequest) -> dict:
    out: dict = {}
    out["PredictorArn"] = value["predictor_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAccuracyMetricsRequest:
    out: GetAccuracyMetricsRequest = {}  # type: ignore[typeddict-item]
    if "PredictorArn" in data:
        out["predictor_arn"] = data["PredictorArn"]
    else:
        raise DeserializationError("GetAccuracyMetricsRequest.predictor_arn required")
    return out
