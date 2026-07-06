"""Generated from Smithy shape ``com.amazonaws.iot#Behavior``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.behavior_criteria
    import aws_sdk_iot.types.behavior_metric
    import aws_sdk_iot.types.behavior_name
    import aws_sdk_iot.types.export_metric
    import aws_sdk_iot.types.metric_dimension
    import aws_sdk_iot.types.suppress_alerts


class Behavior(TypedDict, closed=True):
    name: "aws_sdk_iot.types.behavior_name.BehaviorName"
    """<p>The name you've given to the behavior.</p>"""
    metric: NotRequired["aws_sdk_iot.types.behavior_metric.BehaviorMetric"]
    """<p>What is measured by the behavior.</p>"""
    metric_dimension: NotRequired["aws_sdk_iot.types.metric_dimension.MetricDimension"]
    """<p>The dimension for a metric in your behavior. For example, using a <code>TOPIC_FILTER</code> dimension, you can narrow down the scope of the metric to only MQTT topics where the name matches the pattern specified in the dimension. This can't be used with custom metrics.</p>"""
    criteria: NotRequired["aws_sdk_iot.types.behavior_criteria.BehaviorCriteria"]
    """<p>The criteria that determine if a device is behaving normally in regard to the <code>metric</code>.</p> <note> <p>In the IoT console, you can choose to be sent an alert through Amazon SNS when IoT Device Defender detects that a device is behaving anomalously.</p> </note>"""
    suppress_alerts: NotRequired["aws_sdk_iot.types.suppress_alerts.SuppressAlerts"]
    """<p> Suppresses alerts. </p>"""
    export_metric: NotRequired["aws_sdk_iot.types.export_metric.ExportMetric"]
    """<p>Value indicates exporting metrics related to the behavior when it is true.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Behavior) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "metric" in value:
        out["metric"] = value["metric"]
    if "metric_dimension" in value:
        import aws_sdk_iot.types.metric_dimension

        out["metricDimension"] = aws_sdk_iot.types.metric_dimension.serialize_json(
            value["metric_dimension"]
        )
    if "criteria" in value:
        import aws_sdk_iot.types.behavior_criteria

        out["criteria"] = aws_sdk_iot.types.behavior_criteria.serialize_json(
            value["criteria"]
        )
    if "suppress_alerts" in value:
        out["suppressAlerts"] = value["suppress_alerts"]
    if "export_metric" in value:
        out["exportMetric"] = value["export_metric"]
    return out


def deserialize_json(data: dict) -> Behavior:
    out: Behavior = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("Behavior.name required")
    if "metric" in data:
        out["metric"] = data["metric"]
    if "metricDimension" in data:
        import aws_sdk_iot.types.metric_dimension

        out["metric_dimension"] = aws_sdk_iot.types.metric_dimension.deserialize_json(
            data["metricDimension"]
        )
    if "criteria" in data:
        import aws_sdk_iot.types.behavior_criteria

        out["criteria"] = aws_sdk_iot.types.behavior_criteria.deserialize_json(
            data["criteria"]
        )
    if "suppressAlerts" in data:
        out["suppress_alerts"] = data["suppressAlerts"]
    if "exportMetric" in data:
        out["export_metric"] = data["exportMetric"]
    return out
