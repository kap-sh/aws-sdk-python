"""Generated from Smithy shape ``com.amazonaws.forecast#MonitorDataSource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_forecast.types.arn


class MonitorDataSource(TypedDict):
    dataset_import_job_arn: NotRequired["aws_sdk_forecast.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the dataset import job used to import the data that initiated the monitor evaluation.</p>"""
    forecast_arn: NotRequired["aws_sdk_forecast.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the forecast the monitor used during the evaluation.</p>"""
    predictor_arn: NotRequired["aws_sdk_forecast.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the predictor resource you are monitoring.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MonitorDataSource) -> dict:
    out: dict = {}
    if "dataset_import_job_arn" in value:
        out["DatasetImportJobArn"] = value["dataset_import_job_arn"]
    if "forecast_arn" in value:
        out["ForecastArn"] = value["forecast_arn"]
    if "predictor_arn" in value:
        out["PredictorArn"] = value["predictor_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MonitorDataSource:
    out: MonitorDataSource = {}  # type: ignore[typeddict-item]
    if "DatasetImportJobArn" in data:
        out["dataset_import_job_arn"] = data["DatasetImportJobArn"]
    if "ForecastArn" in data:
        out["forecast_arn"] = data["ForecastArn"]
    if "PredictorArn" in data:
        out["predictor_arn"] = data["PredictorArn"]
    return out
