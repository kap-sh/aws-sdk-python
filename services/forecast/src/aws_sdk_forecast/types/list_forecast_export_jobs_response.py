"""Generated from Smithy shape ``com.amazonaws.forecast#ListForecastExportJobsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_forecast.types.forecast_export_jobs
    import aws_sdk_forecast.types.next_token


class ListForecastExportJobsResponse(TypedDict):
    forecast_export_jobs: NotRequired[
        "aws_sdk_forecast.types.forecast_export_jobs.ForecastExportJobs"
    ]
    """<p>An array of objects that summarize each export job's properties.</p>"""
    next_token: NotRequired["aws_sdk_forecast.types.next_token.NextToken"]
    """<p>If the response is truncated, Amazon Forecast returns this token. To retrieve the next set of results, use the token in the next request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListForecastExportJobsResponse) -> dict:
    out: dict = {}
    if "forecast_export_jobs" in value:
        import aws_sdk_forecast.types.forecast_export_jobs

        out["ForecastExportJobs"] = (
            aws_sdk_forecast.types.forecast_export_jobs.serialize_aws_json_1_1(
                value["forecast_export_jobs"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListForecastExportJobsResponse:
    out: ListForecastExportJobsResponse = {}  # type: ignore[typeddict-item]
    if "ForecastExportJobs" in data:
        import aws_sdk_forecast.types.forecast_export_jobs

        out["forecast_export_jobs"] = (
            aws_sdk_forecast.types.forecast_export_jobs.deserialize_aws_json_1_1(
                data["ForecastExportJobs"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
