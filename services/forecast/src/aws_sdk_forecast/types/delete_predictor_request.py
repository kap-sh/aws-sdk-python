"""Generated from Smithy shape ``com.amazonaws.forecast#DeletePredictorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_forecast.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_forecast.types.arn


class DeletePredictorRequest(TypedDict, closed=True):
    predictor_arn: "aws_sdk_forecast.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the predictor to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeletePredictorRequest) -> dict:
    out: dict = {}
    out["PredictorArn"] = value["predictor_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeletePredictorRequest:
    out: DeletePredictorRequest = {}  # type: ignore[typeddict-item]
    if "PredictorArn" in data:
        out["predictor_arn"] = data["PredictorArn"]
    else:
        raise DeserializationError("DeletePredictorRequest.predictor_arn required")
    return out
