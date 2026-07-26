"""Generated from Smithy shape ``com.amazonaws.forecast#PredictorExecution``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_forecast.types.arn
    import capo_forecast.types.test_window_details


class PredictorExecution(TypedDict, closed=True):
    algorithm_arn: NotRequired["capo_forecast.types.arn.Arn"]
    """<p>The ARN of the algorithm used to test the predictor.</p>"""
    test_windows: NotRequired[
        "capo_forecast.types.test_window_details.TestWindowDetails"
    ]
    """<p>An array of test windows used to evaluate the algorithm. The <code>NumberOfBacktestWindows</code> from the object determines the number of windows in the array.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PredictorExecution) -> dict:
    out: dict = {}
    if "algorithm_arn" in value:
        out["AlgorithmArn"] = value["algorithm_arn"]
    if "test_windows" in value:
        import capo_forecast.types.test_window_details

        out["TestWindows"] = (
            capo_forecast.types.test_window_details.serialize_aws_json_1_1(
                value["test_windows"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PredictorExecution:
    out: PredictorExecution = {}  # type: ignore[typeddict-item]
    if "AlgorithmArn" in data:
        out["algorithm_arn"] = data["AlgorithmArn"]
    if "TestWindows" in data:
        import capo_forecast.types.test_window_details

        out["test_windows"] = (
            capo_forecast.types.test_window_details.deserialize_aws_json_1_1(
                data["TestWindows"]
            )
        )
    return out
