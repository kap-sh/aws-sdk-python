"""Generated from Smithy shape ``com.amazonaws.forecast#DeletePredictorBacktestExportJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_forecast.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_forecast.types.arn


class DeletePredictorBacktestExportJobRequest(TypedDict):
    predictor_backtest_export_job_arn: "aws_sdk_forecast.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the predictor backtest export job to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeletePredictorBacktestExportJobRequest) -> dict:
    out: dict = {}
    out["PredictorBacktestExportJobArn"] = value["predictor_backtest_export_job_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeletePredictorBacktestExportJobRequest:
    out: DeletePredictorBacktestExportJobRequest = {}  # type: ignore[typeddict-item]
    if "PredictorBacktestExportJobArn" in data:
        out["predictor_backtest_export_job_arn"] = data["PredictorBacktestExportJobArn"]
    else:
        raise DeserializationError(
            "DeletePredictorBacktestExportJobRequest.predictor_backtest_export_job_arn required"
        )
    return out
