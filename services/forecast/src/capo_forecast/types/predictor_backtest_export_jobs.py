"""Generated from Smithy shape ``com.amazonaws.forecast#PredictorBacktestExportJobs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_forecast.types.predictor_backtest_export_job_summary

PredictorBacktestExportJobs: TypeAlias = list[
    "capo_forecast.types.predictor_backtest_export_job_summary.PredictorBacktestExportJobSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PredictorBacktestExportJobs) -> list:
    import capo_forecast.types.predictor_backtest_export_job_summary

    out: list = []
    for item in value:
        out.append(
            capo_forecast.types.predictor_backtest_export_job_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PredictorBacktestExportJobs:
    import capo_forecast.types.predictor_backtest_export_job_summary

    out: PredictorBacktestExportJobs = []
    for item in data:
        out.append(
            capo_forecast.types.predictor_backtest_export_job_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
