"""Generated from Smithy shape ``com.amazonaws.frauddetector#TFITrainingMetricsValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.tfi_metric_data_points_list
    import capo_frauddetector.types.tfi_model_performance


class TFITrainingMetricsValue(TypedDict, closed=True):
    metric_data_points: NotRequired[
        "capo_frauddetector.types.tfi_metric_data_points_list.TFIMetricDataPointsList"
    ]
    """<p> The model's performance metrics data points. </p>"""
    model_performance: NotRequired[
        "capo_frauddetector.types.tfi_model_performance.TFIModelPerformance"
    ]
    """<p> The model performance score. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TFITrainingMetricsValue) -> dict:
    out: dict = {}
    if "metric_data_points" in value:
        import capo_frauddetector.types.tfi_metric_data_points_list

        out["metricDataPoints"] = (
            capo_frauddetector.types.tfi_metric_data_points_list.serialize_aws_json_1_1(
                value["metric_data_points"]
            )
        )
    if "model_performance" in value:
        import capo_frauddetector.types.tfi_model_performance

        out["modelPerformance"] = (
            capo_frauddetector.types.tfi_model_performance.serialize_aws_json_1_1(
                value["model_performance"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TFITrainingMetricsValue:
    out: TFITrainingMetricsValue = {}  # type: ignore[typeddict-item]
    if "metricDataPoints" in data:
        import capo_frauddetector.types.tfi_metric_data_points_list

        out["metric_data_points"] = (
            capo_frauddetector.types.tfi_metric_data_points_list.deserialize_aws_json_1_1(
                data["metricDataPoints"]
            )
        )
    if "modelPerformance" in data:
        import capo_frauddetector.types.tfi_model_performance

        out["model_performance"] = (
            capo_frauddetector.types.tfi_model_performance.deserialize_aws_json_1_1(
                data["modelPerformance"]
            )
        )
    return out
