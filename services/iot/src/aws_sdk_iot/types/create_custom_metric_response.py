"""Generated from Smithy shape ``com.amazonaws.iot#CreateCustomMetricResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.custom_metric_arn
    import aws_sdk_iot.types.metric_name


class CreateCustomMetricResponse(TypedDict, closed=True):
    metric_name: NotRequired["aws_sdk_iot.types.metric_name.MetricName"]
    """<p> The name of the custom metric to be used in the metric report. </p>"""
    metric_arn: NotRequired["aws_sdk_iot.types.custom_metric_arn.CustomMetricArn"]
    """<p> The Amazon Resource Number (ARN) of the custom metric. For example, <code>arn:<i>aws-partition</i>:iot:<i>region</i>:<i>accountId</i>:custommetric/<i>metricName</i> </code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCustomMetricResponse) -> dict:
    out: dict = {}
    if "metric_name" in value:
        out["metricName"] = value["metric_name"]
    if "metric_arn" in value:
        out["metricArn"] = value["metric_arn"]
    return out


def deserialize_json(data: dict) -> CreateCustomMetricResponse:
    out: CreateCustomMetricResponse = {}  # type: ignore[typeddict-item]
    if "metricName" in data:
        out["metric_name"] = data["metricName"]
    if "metricArn" in data:
        out["metric_arn"] = data["metricArn"]
    return out
