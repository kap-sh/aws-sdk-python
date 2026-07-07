"""Generated from Smithy shape ``com.amazonaws.costexplorer#ForecastResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.date_interval
    import aws_sdk_cost_explorer.types.generic_string


class ForecastResult(TypedDict, closed=True):
    time_period: NotRequired["aws_sdk_cost_explorer.types.date_interval.DateInterval"]
    """<p>The period of time that the forecast covers.</p>"""
    mean_value: NotRequired["aws_sdk_cost_explorer.types.generic_string.GenericString"]
    """<p>The mean value of the forecast.</p>"""
    prediction_interval_lower_bound: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The lower limit for the prediction interval. </p>"""
    prediction_interval_upper_bound: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The upper limit for the prediction interval. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ForecastResult) -> dict:
    out: dict = {}
    if "time_period" in value:
        import aws_sdk_cost_explorer.types.date_interval

        out["TimePeriod"] = (
            aws_sdk_cost_explorer.types.date_interval.serialize_aws_json_1_1(
                value["time_period"]
            )
        )
    if "mean_value" in value:
        out["MeanValue"] = value["mean_value"]
    if "prediction_interval_lower_bound" in value:
        out["PredictionIntervalLowerBound"] = value["prediction_interval_lower_bound"]
    if "prediction_interval_upper_bound" in value:
        out["PredictionIntervalUpperBound"] = value["prediction_interval_upper_bound"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ForecastResult:
    out: ForecastResult = {}  # type: ignore[typeddict-item]
    if "TimePeriod" in data:
        import aws_sdk_cost_explorer.types.date_interval

        out["time_period"] = (
            aws_sdk_cost_explorer.types.date_interval.deserialize_aws_json_1_1(
                data["TimePeriod"]
            )
        )
    if "MeanValue" in data:
        out["mean_value"] = data["MeanValue"]
    if "PredictionIntervalLowerBound" in data:
        out["prediction_interval_lower_bound"] = data["PredictionIntervalLowerBound"]
    if "PredictionIntervalUpperBound" in data:
        out["prediction_interval_upper_bound"] = data["PredictionIntervalUpperBound"]
    return out
