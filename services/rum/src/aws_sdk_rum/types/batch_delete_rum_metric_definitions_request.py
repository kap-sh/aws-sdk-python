"""Generated from Smithy shape ``com.amazonaws.rum#BatchDeleteRumMetricDefinitionsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_rum.types.app_monitor_name
    import aws_sdk_rum.types.destination_arn
    import aws_sdk_rum.types.metric_definition_ids
    import aws_sdk_rum.types.metric_destination

class BatchDeleteRumMetricDefinitionsRequest(TypedDict):
    app_monitor_name: "aws_sdk_rum.types.app_monitor_name.AppMonitorName"
    """<p>The name of the CloudWatch RUM app monitor that is sending these metrics.</p>"""
    destination: "aws_sdk_rum.types.metric_destination.MetricDestination"
    """<p>Defines the destination where you want to stop sending the specified metrics. Valid values are <code>CloudWatch</code> and <code>Evidently</code>. If you specify <code>Evidently</code>, you must also specify the ARN of the CloudWatchEvidently experiment that is to be the destination and an IAM role that has permission to write to the experiment.</p>"""
    destination_arn: NotRequired["aws_sdk_rum.types.destination_arn.DestinationArn"]
    """<p>This parameter is required if <code>Destination</code> is <code>Evidently</code>. If <code>Destination</code> is <code>CloudWatch</code>, do not use this parameter. </p> <p>This parameter specifies the ARN of the Evidently experiment that was receiving the metrics that are being deleted.</p>"""
    metric_definition_ids: "aws_sdk_rum.types.metric_definition_ids.MetricDefinitionIds"
    """<p>An array of structures which define the metrics that you want to stop sending.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteRumMetricDefinitionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> BatchDeleteRumMetricDefinitionsRequest:
    out: BatchDeleteRumMetricDefinitionsRequest = {}  # type: ignore[typeddict-item]
    return out