"""Generated from Smithy shape ``com.amazonaws.forecast#Baseline``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_forecast.types.predictor_baseline


class Baseline(TypedDict):
    predictor_baseline: NotRequired[
        "aws_sdk_forecast.types.predictor_baseline.PredictorBaseline"
    ]
    r"""<p>The initial <a href=\"https://docs.aws.amazon.com/forecast/latest/dg/metrics.html\">accuracy metrics</a> for the predictor you are monitoring. Use these metrics as a baseline for comparison purposes as you use your predictor and the metrics change.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Baseline) -> dict:
    out: dict = {}
    if "predictor_baseline" in value:
        import aws_sdk_forecast.types.predictor_baseline

        out["PredictorBaseline"] = (
            aws_sdk_forecast.types.predictor_baseline.serialize_aws_json_1_1(
                value["predictor_baseline"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Baseline:
    out: Baseline = {}  # type: ignore[typeddict-item]
    if "PredictorBaseline" in data:
        import aws_sdk_forecast.types.predictor_baseline

        out["predictor_baseline"] = (
            aws_sdk_forecast.types.predictor_baseline.deserialize_aws_json_1_1(
                data["PredictorBaseline"]
            )
        )
    return out
