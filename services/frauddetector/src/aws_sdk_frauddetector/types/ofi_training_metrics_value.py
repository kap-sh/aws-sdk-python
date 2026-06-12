"""Generated from Smithy shape ``com.amazonaws.frauddetector#OFITrainingMetricsValue``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.ofi_metric_data_points_list
    import aws_sdk_frauddetector.types.ofi_model_performance


class OFITrainingMetricsValue(TypedDict):
    metric_data_points: NotRequired[
        "aws_sdk_frauddetector.types.ofi_metric_data_points_list.OFIMetricDataPointsList"
    ]
    """<p> The model's performance metrics data points. </p>"""
    model_performance: NotRequired[
        "aws_sdk_frauddetector.types.ofi_model_performance.OFIModelPerformance"
    ]
    """<p> The model's overall performance score. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OFITrainingMetricsValue) -> dict:
    out: dict = {}
    if "metric_data_points" in value:
        import aws_sdk_frauddetector.types.ofi_metric_data_points_list

        out["metricDataPoints"] = (
            aws_sdk_frauddetector.types.ofi_metric_data_points_list.serialize_aws_json_1_1(
                value["metric_data_points"]
            )
        )
    if "model_performance" in value:
        import aws_sdk_frauddetector.types.ofi_model_performance

        out["modelPerformance"] = (
            aws_sdk_frauddetector.types.ofi_model_performance.serialize_aws_json_1_1(
                value["model_performance"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OFITrainingMetricsValue:
    out: OFITrainingMetricsValue = {}  # type: ignore[typeddict-item]
    if "metricDataPoints" in data:
        import aws_sdk_frauddetector.types.ofi_metric_data_points_list

        out["metric_data_points"] = (
            aws_sdk_frauddetector.types.ofi_metric_data_points_list.deserialize_aws_json_1_1(
                data["metricDataPoints"]
            )
        )
    if "modelPerformance" in data:
        import aws_sdk_frauddetector.types.ofi_model_performance

        out["model_performance"] = (
            aws_sdk_frauddetector.types.ofi_model_performance.deserialize_aws_json_1_1(
                data["modelPerformance"]
            )
        )
    return out
