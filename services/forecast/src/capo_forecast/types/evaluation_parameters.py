"""Generated from Smithy shape ``com.amazonaws.forecast#EvaluationParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_forecast.types.integer


class EvaluationParameters(TypedDict, closed=True):
    number_of_backtest_windows: NotRequired["capo_forecast.types.integer.Integer"]
    """<p>The number of times to split the input data. The default is 1. Valid values are 1 through 5.</p>"""
    back_test_window_offset: NotRequired["capo_forecast.types.integer.Integer"]
    """<p>The point from the end of the dataset where you want to split the data for model training and testing (evaluation). Specify the value as the number of data points. The default is the value of the forecast horizon. <code>BackTestWindowOffset</code> can be used to mimic a past virtual forecast start date. This value must be greater than or equal to the forecast horizon and less than half of the TARGET_TIME_SERIES dataset length.</p> <p> <code>ForecastHorizon</code> <= <code>BackTestWindowOffset</code> < 1/2 * TARGET_TIME_SERIES dataset length</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EvaluationParameters) -> dict:
    out: dict = {}
    if "number_of_backtest_windows" in value:
        out["NumberOfBacktestWindows"] = value["number_of_backtest_windows"]
    if "back_test_window_offset" in value:
        out["BackTestWindowOffset"] = value["back_test_window_offset"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EvaluationParameters:
    out: EvaluationParameters = {}  # type: ignore[typeddict-item]
    if "NumberOfBacktestWindows" in data:
        out["number_of_backtest_windows"] = data["NumberOfBacktestWindows"]
    if "BackTestWindowOffset" in data:
        out["back_test_window_offset"] = data["BackTestWindowOffset"]
    return out
