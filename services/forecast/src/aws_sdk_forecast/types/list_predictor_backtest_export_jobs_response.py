"""Generated from Smithy shape ``com.amazonaws.forecast#ListPredictorBacktestExportJobsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_forecast.types.next_token
    import aws_sdk_forecast.types.predictor_backtest_export_jobs


class ListPredictorBacktestExportJobsResponse(TypedDict):
    predictor_backtest_export_jobs: NotRequired[
        "aws_sdk_forecast.types.predictor_backtest_export_jobs.PredictorBacktestExportJobs"
    ]
    """<p>An array of objects that summarize the properties of each predictor backtest export job.</p>"""
    next_token: NotRequired["aws_sdk_forecast.types.next_token.NextToken"]
    """<p>Returns this token if the response is truncated. To retrieve the next set of results, use the token in the next request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListPredictorBacktestExportJobsResponse) -> dict:
    out: dict = {}
    if "predictor_backtest_export_jobs" in value:
        import aws_sdk_forecast.types.predictor_backtest_export_jobs

        out["PredictorBacktestExportJobs"] = (
            aws_sdk_forecast.types.predictor_backtest_export_jobs.serialize_aws_json_1_1(
                value["predictor_backtest_export_jobs"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListPredictorBacktestExportJobsResponse:
    out: ListPredictorBacktestExportJobsResponse = {}  # type: ignore[typeddict-item]
    if "PredictorBacktestExportJobs" in data:
        import aws_sdk_forecast.types.predictor_backtest_export_jobs

        out["predictor_backtest_export_jobs"] = (
            aws_sdk_forecast.types.predictor_backtest_export_jobs.deserialize_aws_json_1_1(
                data["PredictorBacktestExportJobs"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
