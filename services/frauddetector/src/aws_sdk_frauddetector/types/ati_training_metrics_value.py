"""Generated from Smithy shape ``com.amazonaws.frauddetector#ATITrainingMetricsValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.ati_metric_data_points_list
    import aws_sdk_frauddetector.types.ati_model_performance


class ATITrainingMetricsValue(TypedDict, closed=True):
    metric_data_points: NotRequired[
        "aws_sdk_frauddetector.types.ati_metric_data_points_list.ATIMetricDataPointsList"
    ]
    """<p> The model's performance metrics data points. </p>"""
    model_performance: NotRequired[
        "aws_sdk_frauddetector.types.ati_model_performance.ATIModelPerformance"
    ]
    """<p> The model's overall performance scores. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ATITrainingMetricsValue) -> dict:
    out: dict = {}
    if "metric_data_points" in value:
        import aws_sdk_frauddetector.types.ati_metric_data_points_list

        out["metricDataPoints"] = (
            aws_sdk_frauddetector.types.ati_metric_data_points_list.serialize_aws_json_1_1(
                value["metric_data_points"]
            )
        )
    if "model_performance" in value:
        import aws_sdk_frauddetector.types.ati_model_performance

        out["modelPerformance"] = (
            aws_sdk_frauddetector.types.ati_model_performance.serialize_aws_json_1_1(
                value["model_performance"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ATITrainingMetricsValue:
    out: ATITrainingMetricsValue = {}  # type: ignore[typeddict-item]
    if "metricDataPoints" in data:
        import aws_sdk_frauddetector.types.ati_metric_data_points_list

        out["metric_data_points"] = (
            aws_sdk_frauddetector.types.ati_metric_data_points_list.deserialize_aws_json_1_1(
                data["metricDataPoints"]
            )
        )
    if "modelPerformance" in data:
        import aws_sdk_frauddetector.types.ati_model_performance

        out["model_performance"] = (
            aws_sdk_frauddetector.types.ati_model_performance.deserialize_aws_json_1_1(
                data["modelPerformance"]
            )
        )
    return out
