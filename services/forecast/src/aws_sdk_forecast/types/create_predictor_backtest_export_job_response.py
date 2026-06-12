"""Generated from Smithy shape ``com.amazonaws.forecast#CreatePredictorBacktestExportJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_forecast.types.arn


class CreatePredictorBacktestExportJobResponse(TypedDict):
    predictor_backtest_export_job_arn: NotRequired["aws_sdk_forecast.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the predictor backtest export job that you want to export.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreatePredictorBacktestExportJobResponse) -> dict:
    out: dict = {}
    if "predictor_backtest_export_job_arn" in value:
        out["PredictorBacktestExportJobArn"] = value[
            "predictor_backtest_export_job_arn"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreatePredictorBacktestExportJobResponse:
    out: CreatePredictorBacktestExportJobResponse = {}  # type: ignore[typeddict-item]
    if "PredictorBacktestExportJobArn" in data:
        out["predictor_backtest_export_job_arn"] = data["PredictorBacktestExportJobArn"]
    return out
