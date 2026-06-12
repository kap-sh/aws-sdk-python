"""Generated from Smithy shape ``com.amazonaws.forecast#GetAccuracyMetricsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_forecast.types.auto_ml_override_strategy
    import aws_sdk_forecast.types.boolean
    import aws_sdk_forecast.types.optimization_metric
    import aws_sdk_forecast.types.predictor_evaluation_results


class GetAccuracyMetricsResponse(TypedDict):
    predictor_evaluation_results: NotRequired[
        "aws_sdk_forecast.types.predictor_evaluation_results.PredictorEvaluationResults"
    ]
    """<p>An array of results from evaluating the predictor.</p>"""
    is_auto_predictor: NotRequired["aws_sdk_forecast.types.boolean.Boolean"]
    """<p>Whether the predictor was created with <a>CreateAutoPredictor</a>.</p>"""
    auto_ml_override_strategy: NotRequired[
        "aws_sdk_forecast.types.auto_ml_override_strategy.AutoMLOverrideStrategy"
    ]
    """<note> <p> The <code>LatencyOptimized</code> AutoML override strategy is only available in private beta. Contact Amazon Web Services Support or your account manager to learn more about access privileges. </p> </note> <p>The AutoML strategy used to train the predictor. Unless <code>LatencyOptimized</code> is specified, the AutoML strategy optimizes predictor accuracy.</p> <p>This parameter is only valid for predictors trained using AutoML.</p>"""
    optimization_metric: NotRequired[
        "aws_sdk_forecast.types.optimization_metric.OptimizationMetric"
    ]
    """<p>The accuracy metric used to optimize the predictor.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAccuracyMetricsResponse) -> dict:
    out: dict = {}
    if "predictor_evaluation_results" in value:
        import aws_sdk_forecast.types.predictor_evaluation_results

        out["PredictorEvaluationResults"] = (
            aws_sdk_forecast.types.predictor_evaluation_results.serialize_aws_json_1_1(
                value["predictor_evaluation_results"]
            )
        )
    if "is_auto_predictor" in value:
        out["IsAutoPredictor"] = value["is_auto_predictor"]
    if "auto_ml_override_strategy" in value:
        import aws_sdk_forecast.types.auto_ml_override_strategy

        out["AutoMLOverrideStrategy"] = (
            aws_sdk_forecast.types.auto_ml_override_strategy.serialize_aws_json_1_1(
                value["auto_ml_override_strategy"]
            )
        )
    if "optimization_metric" in value:
        import aws_sdk_forecast.types.optimization_metric

        out["OptimizationMetric"] = (
            aws_sdk_forecast.types.optimization_metric.serialize_aws_json_1_1(
                value["optimization_metric"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAccuracyMetricsResponse:
    out: GetAccuracyMetricsResponse = {}  # type: ignore[typeddict-item]
    if "PredictorEvaluationResults" in data:
        import aws_sdk_forecast.types.predictor_evaluation_results

        out["predictor_evaluation_results"] = (
            aws_sdk_forecast.types.predictor_evaluation_results.deserialize_aws_json_1_1(
                data["PredictorEvaluationResults"]
            )
        )
    if "IsAutoPredictor" in data:
        out["is_auto_predictor"] = data["IsAutoPredictor"]
    if "AutoMLOverrideStrategy" in data:
        import aws_sdk_forecast.types.auto_ml_override_strategy

        out["auto_ml_override_strategy"] = (
            aws_sdk_forecast.types.auto_ml_override_strategy.deserialize_aws_json_1_1(
                data["AutoMLOverrideStrategy"]
            )
        )
    if "OptimizationMetric" in data:
        import aws_sdk_forecast.types.optimization_metric

        out["optimization_metric"] = (
            aws_sdk_forecast.types.optimization_metric.deserialize_aws_json_1_1(
                data["OptimizationMetric"]
            )
        )
    return out
