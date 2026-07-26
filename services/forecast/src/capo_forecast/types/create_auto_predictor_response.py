"""Generated from Smithy shape ``com.amazonaws.forecast#CreateAutoPredictorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_forecast.types.arn


class CreateAutoPredictorResponse(TypedDict, closed=True):
    predictor_arn: NotRequired["capo_forecast.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the predictor.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAutoPredictorResponse) -> dict:
    out: dict = {}
    if "predictor_arn" in value:
        out["PredictorArn"] = value["predictor_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAutoPredictorResponse:
    out: CreateAutoPredictorResponse = {}  # type: ignore[typeddict-item]
    if "PredictorArn" in data:
        out["predictor_arn"] = data["PredictorArn"]
    return out
