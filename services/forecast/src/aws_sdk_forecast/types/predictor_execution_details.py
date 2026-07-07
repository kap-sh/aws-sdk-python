"""Generated from Smithy shape ``com.amazonaws.forecast#PredictorExecutionDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_forecast.types.predictor_executions


class PredictorExecutionDetails(TypedDict, closed=True):
    predictor_executions: NotRequired[
        "aws_sdk_forecast.types.predictor_executions.PredictorExecutions"
    ]
    """<p>An array of the backtests performed to evaluate the accuracy of the predictor against a particular algorithm. The <code>NumberOfBacktestWindows</code> from the object determines the number of windows in the array.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PredictorExecutionDetails) -> dict:
    out: dict = {}
    if "predictor_executions" in value:
        import aws_sdk_forecast.types.predictor_executions

        out["PredictorExecutions"] = (
            aws_sdk_forecast.types.predictor_executions.serialize_aws_json_1_1(
                value["predictor_executions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PredictorExecutionDetails:
    out: PredictorExecutionDetails = {}  # type: ignore[typeddict-item]
    if "PredictorExecutions" in data:
        import aws_sdk_forecast.types.predictor_executions

        out["predictor_executions"] = (
            aws_sdk_forecast.types.predictor_executions.deserialize_aws_json_1_1(
                data["PredictorExecutions"]
            )
        )
    return out
