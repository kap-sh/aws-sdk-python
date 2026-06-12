"""Generated from Smithy shape ``com.amazonaws.frauddetector#TrainingMetrics``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.float
    import aws_sdk_frauddetector.types.metric_data_points_list


class TrainingMetrics(TypedDict):
    auc: NotRequired["aws_sdk_frauddetector.types.float.float"]
    """<p>The area under the curve. This summarizes true positive rate (TPR) and false positive rate (FPR) across all possible model score thresholds. A model with no predictive power has an AUC of 0.5, whereas a perfect model has a score of 1.0.</p>"""
    metric_data_points: NotRequired[
        "aws_sdk_frauddetector.types.metric_data_points_list.metricDataPointsList"
    ]
    """<p>The data points details.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrainingMetrics) -> dict:
    out: dict = {}
    if "auc" in value:
        out["auc"] = value["auc"]
    if "metric_data_points" in value:
        import aws_sdk_frauddetector.types.metric_data_points_list

        out["metricDataPoints"] = (
            aws_sdk_frauddetector.types.metric_data_points_list.serialize_aws_json_1_1(
                value["metric_data_points"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TrainingMetrics:
    out: TrainingMetrics = {}  # type: ignore[typeddict-item]
    if "auc" in data:
        out["auc"] = data["auc"]
    if "metricDataPoints" in data:
        import aws_sdk_frauddetector.types.metric_data_points_list

        out["metric_data_points"] = (
            aws_sdk_frauddetector.types.metric_data_points_list.deserialize_aws_json_1_1(
                data["metricDataPoints"]
            )
        )
    return out
