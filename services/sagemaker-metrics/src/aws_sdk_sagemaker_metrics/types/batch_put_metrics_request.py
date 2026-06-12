"""Generated from Smithy shape ``com.amazonaws.sagemakermetrics#BatchPutMetricsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker_metrics.types.experiment_entity_name
    import aws_sdk_sagemaker_metrics.types.raw_metric_data_list


class BatchPutMetricsRequest(TypedDict):
    trial_component_name: NotRequired[
        "aws_sdk_sagemaker_metrics.types.experiment_entity_name.ExperimentEntityName"
    ]
    """<p>The name of the Trial Component to associate with the metrics. The Trial Component name must be entirely lowercase.</p>"""
    metric_data: NotRequired[
        "aws_sdk_sagemaker_metrics.types.raw_metric_data_list.RawMetricDataList"
    ]
    """<p>A list of raw metric values to put.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchPutMetricsRequest) -> dict:
    out: dict = {}
    if "trial_component_name" in value:
        out["TrialComponentName"] = value["trial_component_name"]
    if "metric_data" in value:
        import aws_sdk_sagemaker_metrics.types.raw_metric_data_list

        out["MetricData"] = (
            aws_sdk_sagemaker_metrics.types.raw_metric_data_list.serialize_json(
                value["metric_data"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchPutMetricsRequest:
    out: BatchPutMetricsRequest = {}  # type: ignore[typeddict-item]
    if "TrialComponentName" in data:
        out["trial_component_name"] = data["TrialComponentName"]
    if "MetricData" in data:
        import aws_sdk_sagemaker_metrics.types.raw_metric_data_list

        out["metric_data"] = (
            aws_sdk_sagemaker_metrics.types.raw_metric_data_list.deserialize_json(
                data["MetricData"]
            )
        )
    return out
