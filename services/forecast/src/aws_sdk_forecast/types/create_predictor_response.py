"""Generated from Smithy shape ``com.amazonaws.forecast#CreatePredictorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_forecast.types.arn


class CreatePredictorResponse(TypedDict, closed=True):
    predictor_arn: NotRequired["aws_sdk_forecast.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the predictor.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreatePredictorResponse) -> dict:
    out: dict = {}
    if "predictor_arn" in value:
        out["PredictorArn"] = value["predictor_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreatePredictorResponse:
    out: CreatePredictorResponse = {}  # type: ignore[typeddict-item]
    if "PredictorArn" in data:
        out["predictor_arn"] = data["PredictorArn"]
    return out
