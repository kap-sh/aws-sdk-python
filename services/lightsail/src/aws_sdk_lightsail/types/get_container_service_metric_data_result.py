"""Generated from Smithy shape ``com.amazonaws.lightsail#GetContainerServiceMetricDataResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.container_service_metric_name
    import aws_sdk_lightsail.types.metric_datapoint_list


class GetContainerServiceMetricDataResult(TypedDict, closed=True):
    metric_name: NotRequired[
        "aws_sdk_lightsail.types.container_service_metric_name.ContainerServiceMetricName"
    ]
    """<p>The name of the metric returned. </p>"""
    metric_data: NotRequired[
        "aws_sdk_lightsail.types.metric_datapoint_list.MetricDatapointList"
    ]
    """<p>An array of objects that describe the metric data returned.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetContainerServiceMetricDataResult) -> dict:
    out: dict = {}
    if "metric_name" in value:
        import aws_sdk_lightsail.types.container_service_metric_name

        out["metricName"] = (
            aws_sdk_lightsail.types.container_service_metric_name.serialize_aws_json_1_1(
                value["metric_name"]
            )
        )
    if "metric_data" in value:
        import aws_sdk_lightsail.types.metric_datapoint_list

        out["metricData"] = (
            aws_sdk_lightsail.types.metric_datapoint_list.serialize_aws_json_1_1(
                value["metric_data"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetContainerServiceMetricDataResult:
    out: GetContainerServiceMetricDataResult = {}  # type: ignore[typeddict-item]
    if "metricName" in data:
        import aws_sdk_lightsail.types.container_service_metric_name

        out["metric_name"] = (
            aws_sdk_lightsail.types.container_service_metric_name.deserialize_aws_json_1_1(
                data["metricName"]
            )
        )
    if "metricData" in data:
        import aws_sdk_lightsail.types.metric_datapoint_list

        out["metric_data"] = (
            aws_sdk_lightsail.types.metric_datapoint_list.deserialize_aws_json_1_1(
                data["metricData"]
            )
        )
    return out
