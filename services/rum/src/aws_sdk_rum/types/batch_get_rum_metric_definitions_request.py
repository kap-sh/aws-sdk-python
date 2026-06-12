"""Generated from Smithy shape ``com.amazonaws.rum#BatchGetRumMetricDefinitionsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_rum.types.app_monitor_name
    import aws_sdk_rum.types.destination_arn
    import aws_sdk_rum.types.max_results_integer
    import aws_sdk_rum.types.metric_destination

class BatchGetRumMetricDefinitionsRequest(TypedDict):
    app_monitor_name: "aws_sdk_rum.types.app_monitor_name.AppMonitorName"
    """<p>The name of the CloudWatch RUM app monitor that is sending the metrics.</p>"""
    destination: "aws_sdk_rum.types.metric_destination.MetricDestination"
    """<p>The type of destination that you want to view metrics for. Valid values are <code>CloudWatch</code> and <code>Evidently</code>.</p>"""
    destination_arn: NotRequired["aws_sdk_rum.types.destination_arn.DestinationArn"]
    """<p>This parameter is required if <code>Destination</code> is <code>Evidently</code>. If <code>Destination</code> is <code>CloudWatch</code>, do not use this parameter.</p> <p>This parameter specifies the ARN of the Evidently experiment that corresponds to the destination.</p>"""
    max_results: NotRequired["aws_sdk_rum.types.max_results_integer.MaxResultsInteger"]
    """<p>The maximum number of results to return in one operation. The default is 50. The maximum that you can specify is 100.</p> <p>To retrieve the remaining results, make another call with the returned <code>NextToken</code> value. </p>"""
    next_token: NotRequired["str"]
    """<p>Use the token returned by the previous operation to request the next page of results.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: BatchGetRumMetricDefinitionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> BatchGetRumMetricDefinitionsRequest:
    out: BatchGetRumMetricDefinitionsRequest = {}  # type: ignore[typeddict-item]
    return out