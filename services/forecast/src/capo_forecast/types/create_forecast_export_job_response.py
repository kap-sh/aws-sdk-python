"""Generated from Smithy shape ``com.amazonaws.forecast#CreateForecastExportJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_forecast.types.arn


class CreateForecastExportJobResponse(TypedDict, closed=True):
    forecast_export_job_arn: NotRequired["capo_forecast.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the export job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateForecastExportJobResponse) -> dict:
    out: dict = {}
    if "forecast_export_job_arn" in value:
        out["ForecastExportJobArn"] = value["forecast_export_job_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateForecastExportJobResponse:
    out: CreateForecastExportJobResponse = {}  # type: ignore[typeddict-item]
    if "ForecastExportJobArn" in data:
        out["forecast_export_job_arn"] = data["ForecastExportJobArn"]
    return out
