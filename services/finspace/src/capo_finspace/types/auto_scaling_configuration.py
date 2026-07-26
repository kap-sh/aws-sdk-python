"""Generated from Smithy shape ``com.amazonaws.finspace#AutoScalingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_finspace.types.auto_scaling_metric
    import capo_finspace.types.auto_scaling_metric_target
    import capo_finspace.types.cooldown_time
    import capo_finspace.types.node_count


class AutoScalingConfiguration(TypedDict, closed=True):
    min_node_count: NotRequired["capo_finspace.types.node_count.NodeCount"]
    """<p>The lowest number of nodes to scale. This value must be at least 1 and less than the <code>maxNodeCount</code>. If the nodes in a cluster belong to multiple availability zones, then <code>minNodeCount</code> must be at least 3.</p>"""
    max_node_count: NotRequired["capo_finspace.types.node_count.NodeCount"]
    """<p>The highest number of nodes to scale. This value cannot be greater than 5.</p>"""
    auto_scaling_metric: NotRequired[
        "capo_finspace.types.auto_scaling_metric.AutoScalingMetric"
    ]
    """<p> The metric your cluster will track in order to scale in and out. For example, <code>CPU_UTILIZATION_PERCENTAGE</code> is the average CPU usage across all the nodes in a cluster.</p>"""
    metric_target: NotRequired[
        "capo_finspace.types.auto_scaling_metric_target.AutoScalingMetricTarget"
    ]
    """<p>The desired value of the chosen <code>autoScalingMetric</code>. When the metric drops below this value, the cluster will scale in. When the metric goes above this value, the cluster will scale out. You can set the target value between 1 and 100 percent.</p>"""
    scale_in_cooldown_seconds: NotRequired[
        "capo_finspace.types.cooldown_time.CooldownTime"
    ]
    """<p>The duration in seconds that FinSpace will wait after a scale in event before initiating another scaling event.</p>"""
    scale_out_cooldown_seconds: NotRequired[
        "capo_finspace.types.cooldown_time.CooldownTime"
    ]
    """<p>The duration in seconds that FinSpace will wait after a scale out event before initiating another scaling event.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutoScalingConfiguration) -> dict:
    out: dict = {}
    if "min_node_count" in value:
        out["minNodeCount"] = value["min_node_count"]
    if "max_node_count" in value:
        out["maxNodeCount"] = value["max_node_count"]
    if "auto_scaling_metric" in value:
        import capo_finspace.types.auto_scaling_metric

        out["autoScalingMetric"] = (
            capo_finspace.types.auto_scaling_metric.serialize_json(
                value["auto_scaling_metric"]
            )
        )
    if "metric_target" in value:
        out["metricTarget"] = value["metric_target"]
    if "scale_in_cooldown_seconds" in value:
        out["scaleInCooldownSeconds"] = value["scale_in_cooldown_seconds"]
    if "scale_out_cooldown_seconds" in value:
        out["scaleOutCooldownSeconds"] = value["scale_out_cooldown_seconds"]
    return out


def deserialize_json(data: dict) -> AutoScalingConfiguration:
    out: AutoScalingConfiguration = {}  # type: ignore[typeddict-item]
    if "minNodeCount" in data:
        out["min_node_count"] = data["minNodeCount"]
    if "maxNodeCount" in data:
        out["max_node_count"] = data["maxNodeCount"]
    if "autoScalingMetric" in data:
        import capo_finspace.types.auto_scaling_metric

        out["auto_scaling_metric"] = (
            capo_finspace.types.auto_scaling_metric.deserialize_json(
                data["autoScalingMetric"]
            )
        )
    if "metricTarget" in data:
        out["metric_target"] = data["metricTarget"]
    if "scaleInCooldownSeconds" in data:
        out["scale_in_cooldown_seconds"] = data["scaleInCooldownSeconds"]
    if "scaleOutCooldownSeconds" in data:
        out["scale_out_cooldown_seconds"] = data["scaleOutCooldownSeconds"]
    return out
