"""Generated from Smithy shape ``com.amazonaws.forecast#ForecastExportJobs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_forecast.types.forecast_export_job_summary

ForecastExportJobs: TypeAlias = list[
    "capo_forecast.types.forecast_export_job_summary.ForecastExportJobSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ForecastExportJobs) -> list:
    import capo_forecast.types.forecast_export_job_summary

    out: list = []
    for item in value:
        out.append(
            capo_forecast.types.forecast_export_job_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ForecastExportJobs:
    import capo_forecast.types.forecast_export_job_summary

    out: ForecastExportJobs = []
    for item in data:
        out.append(
            capo_forecast.types.forecast_export_job_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
