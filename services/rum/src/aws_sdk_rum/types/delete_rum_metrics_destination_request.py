"""Generated from Smithy shape ``com.amazonaws.rum#DeleteRumMetricsDestinationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rum.types.app_monitor_name
    import aws_sdk_rum.types.destination_arn
    import aws_sdk_rum.types.metric_destination


class DeleteRumMetricsDestinationRequest(TypedDict):
    app_monitor_name: "aws_sdk_rum.types.app_monitor_name.AppMonitorName"
    """<p>The name of the app monitor that is sending metrics to the destination that you want to delete.</p>"""
    destination: "aws_sdk_rum.types.metric_destination.MetricDestination"
    """<p>The type of destination to delete. Valid values are <code>CloudWatch</code> and <code>Evidently</code>.</p>"""
    destination_arn: NotRequired["aws_sdk_rum.types.destination_arn.DestinationArn"]
    """<p>This parameter is required if <code>Destination</code> is <code>Evidently</code>. If <code>Destination</code> is <code>CloudWatch</code>, do not use this parameter. This parameter specifies the ARN of the Evidently experiment that corresponds to the destination to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRumMetricsDestinationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteRumMetricsDestinationRequest:
    out: DeleteRumMetricsDestinationRequest = {}  # type: ignore[typeddict-item]
    return out
