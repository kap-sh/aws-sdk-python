"""Generated from Smithy shape ``com.amazonaws.costexplorer#GetCostForecastResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.forecast_results_by_time
    import aws_sdk_cost_explorer.types.metric_value


class GetCostForecastResponse(TypedDict):
    total: NotRequired["aws_sdk_cost_explorer.types.metric_value.MetricValue"]
    """<p>How much you are forecasted to spend over the forecast period, in <code>USD</code>.</p>"""
    forecast_results_by_time: NotRequired[
        "aws_sdk_cost_explorer.types.forecast_results_by_time.ForecastResultsByTime"
    ]
    """<p>The forecasts for your query, in order. For <code>DAILY</code> forecasts, this is a list of days. For <code>MONTHLY</code> forecasts, this is a list of months.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCostForecastResponse) -> dict:
    out: dict = {}
    if "total" in value:
        import aws_sdk_cost_explorer.types.metric_value

        out["Total"] = aws_sdk_cost_explorer.types.metric_value.serialize_aws_json_1_1(
            value["total"]
        )
    if "forecast_results_by_time" in value:
        import aws_sdk_cost_explorer.types.forecast_results_by_time

        out["ForecastResultsByTime"] = (
            aws_sdk_cost_explorer.types.forecast_results_by_time.serialize_aws_json_1_1(
                value["forecast_results_by_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCostForecastResponse:
    out: GetCostForecastResponse = {}  # type: ignore[typeddict-item]
    if "Total" in data:
        import aws_sdk_cost_explorer.types.metric_value

        out["total"] = (
            aws_sdk_cost_explorer.types.metric_value.deserialize_aws_json_1_1(
                data["Total"]
            )
        )
    if "ForecastResultsByTime" in data:
        import aws_sdk_cost_explorer.types.forecast_results_by_time

        out["forecast_results_by_time"] = (
            aws_sdk_cost_explorer.types.forecast_results_by_time.deserialize_aws_json_1_1(
                data["ForecastResultsByTime"]
            )
        )
    return out
