"""Generated from Smithy shape ``com.amazonaws.sagemaker#CandidateArtifactLocations``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.backtest_results_location
    import capo_sagemaker.types.explainability_location
    import capo_sagemaker.types.model_insights_location


class CandidateArtifactLocations(TypedDict, closed=True):
    explainability: NotRequired[
        "capo_sagemaker.types.explainability_location.ExplainabilityLocation"
    ]
    """<p>The Amazon S3 prefix to the explainability artifacts generated for the AutoML candidate.</p>"""
    model_insights: NotRequired[
        "capo_sagemaker.types.model_insights_location.ModelInsightsLocation"
    ]
    """<p>The Amazon S3 prefix to the model insight artifacts generated for the AutoML candidate.</p>"""
    backtest_results: NotRequired[
        "capo_sagemaker.types.backtest_results_location.BacktestResultsLocation"
    ]
    """<p>The Amazon S3 prefix to the accuracy metrics and the inference results observed over the testing window. Available only for the time-series forecasting problem type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CandidateArtifactLocations) -> dict:
    out: dict = {}
    if "explainability" in value:
        out["Explainability"] = value["explainability"]
    if "model_insights" in value:
        out["ModelInsights"] = value["model_insights"]
    if "backtest_results" in value:
        out["BacktestResults"] = value["backtest_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CandidateArtifactLocations:
    out: CandidateArtifactLocations = {}  # type: ignore[typeddict-item]
    if "Explainability" in data:
        out["explainability"] = data["Explainability"]
    if "ModelInsights" in data:
        out["model_insights"] = data["ModelInsights"]
    if "BacktestResults" in data:
        out["backtest_results"] = data["BacktestResults"]
    return out
