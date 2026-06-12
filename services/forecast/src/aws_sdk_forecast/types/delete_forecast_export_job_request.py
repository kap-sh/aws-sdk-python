"""Generated from Smithy shape ``com.amazonaws.forecast#DeleteForecastExportJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_forecast.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_forecast.types.arn


class DeleteForecastExportJobRequest(TypedDict):
    forecast_export_job_arn: "aws_sdk_forecast.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the forecast export job to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteForecastExportJobRequest) -> dict:
    out: dict = {}
    out["ForecastExportJobArn"] = value["forecast_export_job_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteForecastExportJobRequest:
    out: DeleteForecastExportJobRequest = {}  # type: ignore[typeddict-item]
    if "ForecastExportJobArn" in data:
        out["forecast_export_job_arn"] = data["ForecastExportJobArn"]
    else:
        raise DeserializationError(
            "DeleteForecastExportJobRequest.forecast_export_job_arn required"
        )
    return out
