"""Generated from Smithy shape ``com.amazonaws.frauddetector#OFITrainingMetricsValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.ofi_metric_data_points_list
    import capo_frauddetector.types.ofi_model_performance


class OFITrainingMetricsValue(TypedDict, closed=True):
    metric_data_points: NotRequired[
        "capo_frauddetector.types.ofi_metric_data_points_list.OFIMetricDataPointsList"
    ]
    """<p> The model's performance metrics data points. </p>"""
    model_performance: NotRequired[
        "capo_frauddetector.types.ofi_model_performance.OFIModelPerformance"
    ]
    """<p> The model's overall performance score. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OFITrainingMetricsValue) -> dict:
    out: dict = {}
    if "metric_data_points" in value:
        import capo_frauddetector.types.ofi_metric_data_points_list

        out["metricDataPoints"] = (
            capo_frauddetector.types.ofi_metric_data_points_list.serialize_aws_json_1_1(
                value["metric_data_points"]
            )
        )
    if "model_performance" in value:
        import capo_frauddetector.types.ofi_model_performance

        out["modelPerformance"] = (
            capo_frauddetector.types.ofi_model_performance.serialize_aws_json_1_1(
                value["model_performance"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OFITrainingMetricsValue:
    out: OFITrainingMetricsValue = {}  # type: ignore[typeddict-item]
    if "metricDataPoints" in data:
        import capo_frauddetector.types.ofi_metric_data_points_list

        out["metric_data_points"] = (
            capo_frauddetector.types.ofi_metric_data_points_list.deserialize_aws_json_1_1(
                data["metricDataPoints"]
            )
        )
    if "modelPerformance" in data:
        import capo_frauddetector.types.ofi_model_performance

        out["model_performance"] = (
            capo_frauddetector.types.ofi_model_performance.deserialize_aws_json_1_1(
                data["modelPerformance"]
            )
        )
    return out
