"""Generated from Smithy shape ``com.amazonaws.sagemaker#TuningJobCompletionCriteria``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.best_objective_not_improving
    import aws_sdk_sagemaker.types.convergence_detected
    import aws_sdk_sagemaker.types.target_objective_metric_value


class TuningJobCompletionCriteria(TypedDict):
    target_objective_metric_value: NotRequired[
        "aws_sdk_sagemaker.types.target_objective_metric_value.TargetObjectiveMetricValue"
    ]
    """<p>The value of the objective metric.</p>"""
    best_objective_not_improving: NotRequired[
        "aws_sdk_sagemaker.types.best_objective_not_improving.BestObjectiveNotImproving"
    ]
    """<p>A flag to stop your hyperparameter tuning job if model performance fails to improve as evaluated against an objective function.</p>"""
    convergence_detected: NotRequired[
        "aws_sdk_sagemaker.types.convergence_detected.ConvergenceDetected"
    ]
    """<p>A flag to top your hyperparameter tuning job if automatic model tuning (AMT) has detected that your model has converged as evaluated against your objective function.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TuningJobCompletionCriteria) -> dict:
    out: dict = {}
    if "target_objective_metric_value" in value:
        out["TargetObjectiveMetricValue"] = value["target_objective_metric_value"]
    if "best_objective_not_improving" in value:
        import aws_sdk_sagemaker.types.best_objective_not_improving

        out["BestObjectiveNotImproving"] = (
            aws_sdk_sagemaker.types.best_objective_not_improving.serialize_aws_json_1_1(
                value["best_objective_not_improving"]
            )
        )
    if "convergence_detected" in value:
        import aws_sdk_sagemaker.types.convergence_detected

        out["ConvergenceDetected"] = (
            aws_sdk_sagemaker.types.convergence_detected.serialize_aws_json_1_1(
                value["convergence_detected"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TuningJobCompletionCriteria:
    out: TuningJobCompletionCriteria = {}  # type: ignore[typeddict-item]
    if "TargetObjectiveMetricValue" in data:
        out["target_objective_metric_value"] = data["TargetObjectiveMetricValue"]
    if "BestObjectiveNotImproving" in data:
        import aws_sdk_sagemaker.types.best_objective_not_improving

        out["best_objective_not_improving"] = (
            aws_sdk_sagemaker.types.best_objective_not_improving.deserialize_aws_json_1_1(
                data["BestObjectiveNotImproving"]
            )
        )
    if "ConvergenceDetected" in data:
        import aws_sdk_sagemaker.types.convergence_detected

        out["convergence_detected"] = (
            aws_sdk_sagemaker.types.convergence_detected.deserialize_aws_json_1_1(
                data["ConvergenceDetected"]
            )
        )
    return out
