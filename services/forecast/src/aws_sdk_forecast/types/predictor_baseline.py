"""Generated from Smithy shape ``com.amazonaws.forecast#PredictorBaseline``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_forecast.types.baseline_metrics


class PredictorBaseline(TypedDict):
    baseline_metrics: NotRequired[
        "aws_sdk_forecast.types.baseline_metrics.BaselineMetrics"
    ]
    r"""<p>The initial <a href=\"https://docs.aws.amazon.com/forecast/latest/dg/metrics.html\">accuracy metrics</a> for the predictor. Use these metrics as a baseline for comparison purposes as you use your predictor and the metrics change.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PredictorBaseline) -> dict:
    out: dict = {}
    if "baseline_metrics" in value:
        import aws_sdk_forecast.types.baseline_metrics

        out["BaselineMetrics"] = (
            aws_sdk_forecast.types.baseline_metrics.serialize_aws_json_1_1(
                value["baseline_metrics"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PredictorBaseline:
    out: PredictorBaseline = {}  # type: ignore[typeddict-item]
    if "BaselineMetrics" in data:
        import aws_sdk_forecast.types.baseline_metrics

        out["baseline_metrics"] = (
            aws_sdk_forecast.types.baseline_metrics.deserialize_aws_json_1_1(
                data["BaselineMetrics"]
            )
        )
    return out
