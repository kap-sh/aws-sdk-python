"""Generated from Smithy shape ``com.amazonaws.comprehend#FlywheelModelEvaluationMetrics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.double


class FlywheelModelEvaluationMetrics(TypedDict, closed=True):
    average_f1_score: NotRequired["capo_comprehend.types.double.Double"]
    """<p>The average F1 score from the evaluation metrics.</p>"""
    average_precision: NotRequired["capo_comprehend.types.double.Double"]
    """<p>Average precision metric for the model.</p>"""
    average_recall: NotRequired["capo_comprehend.types.double.Double"]
    """<p>Average recall metric for the model.</p>"""
    average_accuracy: NotRequired["capo_comprehend.types.double.Double"]
    """<p>Average accuracy metric for the model.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FlywheelModelEvaluationMetrics) -> dict:
    out: dict = {}
    if "average_f1_score" in value:
        out["AverageF1Score"] = value["average_f1_score"]
    if "average_precision" in value:
        out["AveragePrecision"] = value["average_precision"]
    if "average_recall" in value:
        out["AverageRecall"] = value["average_recall"]
    if "average_accuracy" in value:
        out["AverageAccuracy"] = value["average_accuracy"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FlywheelModelEvaluationMetrics:
    out: FlywheelModelEvaluationMetrics = {}  # type: ignore[typeddict-item]
    if "AverageF1Score" in data:
        out["average_f1_score"] = data["AverageF1Score"]
    if "AveragePrecision" in data:
        out["average_precision"] = data["AveragePrecision"]
    if "AverageRecall" in data:
        out["average_recall"] = data["AverageRecall"]
    if "AverageAccuracy" in data:
        out["average_accuracy"] = data["AverageAccuracy"]
    return out
