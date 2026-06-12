"""Generated from Smithy shape ``com.amazonaws.forecast#EvaluationResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_forecast.types.arn
    import aws_sdk_forecast.types.test_windows


class EvaluationResult(TypedDict):
    algorithm_arn: NotRequired["aws_sdk_forecast.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the algorithm that was evaluated.</p>"""
    test_windows: NotRequired["aws_sdk_forecast.types.test_windows.TestWindows"]
    """<p>The array of test windows used for evaluating the algorithm. The <code>NumberOfBacktestWindows</code> from the <a>EvaluationParameters</a> object determines the number of windows in the array.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EvaluationResult) -> dict:
    out: dict = {}
    if "algorithm_arn" in value:
        out["AlgorithmArn"] = value["algorithm_arn"]
    if "test_windows" in value:
        import aws_sdk_forecast.types.test_windows

        out["TestWindows"] = aws_sdk_forecast.types.test_windows.serialize_aws_json_1_1(
            value["test_windows"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EvaluationResult:
    out: EvaluationResult = {}  # type: ignore[typeddict-item]
    if "AlgorithmArn" in data:
        out["algorithm_arn"] = data["AlgorithmArn"]
    if "TestWindows" in data:
        import aws_sdk_forecast.types.test_windows

        out["test_windows"] = (
            aws_sdk_forecast.types.test_windows.deserialize_aws_json_1_1(
                data["TestWindows"]
            )
        )
    return out
