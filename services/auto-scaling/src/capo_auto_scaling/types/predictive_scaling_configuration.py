"""Generated from Smithy shape ``com.amazonaws.autoscaling#PredictiveScalingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.predictive_scaling_max_capacity_breach_behavior
    import capo_auto_scaling.types.predictive_scaling_max_capacity_buffer
    import capo_auto_scaling.types.predictive_scaling_metric_specifications
    import capo_auto_scaling.types.predictive_scaling_mode
    import capo_auto_scaling.types.predictive_scaling_scheduling_buffer_time


class PredictiveScalingConfiguration(TypedDict, closed=True):
    metric_specifications: NotRequired[
        "capo_auto_scaling.types.predictive_scaling_metric_specifications.PredictiveScalingMetricSpecifications"
    ]
    """<p>This structure includes the metrics and target utilization to use for predictive scaling. </p> <p>This is an array, but we currently only support a single metric specification. That is, you can specify a target value and a single metric pair, or a target value and one scaling metric and one load metric.</p>"""
    mode: NotRequired[
        "capo_auto_scaling.types.predictive_scaling_mode.PredictiveScalingMode"
    ]
    """<p>The predictive scaling mode. Defaults to <code>ForecastOnly</code> if not specified.</p>"""
    scheduling_buffer_time: NotRequired[
        "capo_auto_scaling.types.predictive_scaling_scheduling_buffer_time.PredictiveScalingSchedulingBufferTime"
    ]
    """<p>The amount of time, in seconds, by which the instance launch time can be advanced. For example, the forecast says to add capacity at 10:00 AM, and you choose to pre-launch instances by 5 minutes. In that case, the instances will be launched at 9:55 AM. The intention is to give resources time to be provisioned. It can take a few minutes to launch an EC2 instance. The actual amount of time required depends on several factors, such as the size of the instance and whether there are startup scripts to complete. </p> <p>The value must be less than the forecast interval duration of 3600 seconds (60 minutes). Defaults to 300 seconds if not specified. </p>"""
    max_capacity_breach_behavior: NotRequired[
        "capo_auto_scaling.types.predictive_scaling_max_capacity_breach_behavior.PredictiveScalingMaxCapacityBreachBehavior"
    ]
    """<p>Defines the behavior that should be applied if the forecast capacity approaches or exceeds the maximum capacity of the Auto Scaling group. Defaults to <code>HonorMaxCapacity</code> if not specified.</p> <p>The following are possible values:</p> <ul> <li> <p> <code>HonorMaxCapacity</code> - Amazon EC2 Auto Scaling can't increase the maximum capacity of the group when the forecast capacity is close to or exceeds the maximum capacity.</p> </li> <li> <p> <code>IncreaseMaxCapacity</code> - Amazon EC2 Auto Scaling can increase the maximum capacity of the group when the forecast capacity is close to or exceeds the maximum capacity. The upper limit is determined by the forecasted capacity and the value for <code>MaxCapacityBuffer</code>.</p> </li> </ul> <important> <p>Use caution when allowing the maximum capacity to be automatically increased. This can lead to more instances being launched than intended if the increased maximum capacity is not monitored and managed. The increased maximum capacity then becomes the new normal maximum capacity for the Auto Scaling group until you manually update it. The maximum capacity does not automatically decrease back to the original maximum.</p> </important>"""
    max_capacity_buffer: NotRequired[
        "capo_auto_scaling.types.predictive_scaling_max_capacity_buffer.PredictiveScalingMaxCapacityBuffer"
    ]
    """<p>The size of the capacity buffer to use when the forecast capacity is close to or exceeds the maximum capacity. The value is specified as a percentage relative to the forecast capacity. For example, if the buffer is 10, this means a 10 percent buffer, such that if the forecast capacity is 50, and the maximum capacity is 40, then the effective maximum capacity is 55.</p> <p>If set to 0, Amazon EC2 Auto Scaling may scale capacity higher than the maximum capacity to equal but not exceed forecast capacity. </p> <p>Required if the <code>MaxCapacityBreachBehavior</code> property is set to <code>IncreaseMaxCapacity</code>, and cannot be used otherwise.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PredictiveScalingConfiguration, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "metric_specifications" in value:
        import capo_auto_scaling.types.predictive_scaling_metric_specifications

        capo_auto_scaling.types.predictive_scaling_metric_specifications.serialize_query(
            value["metric_specifications"], pairs, f"{prefix}.MetricSpecifications"
        )
    if "mode" in value:
        import capo_auto_scaling.types.predictive_scaling_mode

        capo_auto_scaling.types.predictive_scaling_mode.serialize_query(
            value["mode"], pairs, f"{prefix}.Mode"
        )
    if "scheduling_buffer_time" in value:
        pairs.append(
            (f"{prefix}.SchedulingBufferTime", str(value["scheduling_buffer_time"]))
        )
    if "max_capacity_breach_behavior" in value:
        import capo_auto_scaling.types.predictive_scaling_max_capacity_breach_behavior

        capo_auto_scaling.types.predictive_scaling_max_capacity_breach_behavior.serialize_query(
            value["max_capacity_breach_behavior"],
            pairs,
            f"{prefix}.MaxCapacityBreachBehavior",
        )
    if "max_capacity_buffer" in value:
        pairs.append((f"{prefix}.MaxCapacityBuffer", str(value["max_capacity_buffer"])))


def deserialize_query(el: Element) -> PredictiveScalingConfiguration:
    out: PredictiveScalingConfiguration = {}  # type: ignore[typeddict-item]
    child_metric_specifications = el.find("MetricSpecifications")
    if child_metric_specifications is not None:
        import capo_auto_scaling.types.predictive_scaling_metric_specifications

        out["metric_specifications"] = (
            capo_auto_scaling.types.predictive_scaling_metric_specifications.deserialize_query(
                child_metric_specifications
            )
        )
    child_mode = el.find("Mode")
    if child_mode is not None:
        import capo_auto_scaling.types.predictive_scaling_mode

        out["mode"] = capo_auto_scaling.types.predictive_scaling_mode.deserialize_query(
            child_mode
        )
    child_scheduling_buffer_time = el.find("SchedulingBufferTime")
    if child_scheduling_buffer_time is not None:
        out["scheduling_buffer_time"] = int(child_scheduling_buffer_time.text or "")
    child_max_capacity_breach_behavior = el.find("MaxCapacityBreachBehavior")
    if child_max_capacity_breach_behavior is not None:
        import capo_auto_scaling.types.predictive_scaling_max_capacity_breach_behavior

        out["max_capacity_breach_behavior"] = (
            capo_auto_scaling.types.predictive_scaling_max_capacity_breach_behavior.deserialize_query(
                child_max_capacity_breach_behavior
            )
        )
    child_max_capacity_buffer = el.find("MaxCapacityBuffer")
    if child_max_capacity_buffer is not None:
        out["max_capacity_buffer"] = int(child_max_capacity_buffer.text or "")
    return out
