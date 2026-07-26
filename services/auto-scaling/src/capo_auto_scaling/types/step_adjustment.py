"""Generated from Smithy shape ``com.amazonaws.autoscaling#StepAdjustment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.metric_scale
    import capo_auto_scaling.types.policy_increment


class StepAdjustment(TypedDict, closed=True):
    metric_interval_lower_bound: NotRequired[
        "capo_auto_scaling.types.metric_scale.MetricScale"
    ]
    """<p>The lower bound for the difference between the alarm threshold and the CloudWatch metric. If the metric value is above the breach threshold, the lower bound is inclusive (the metric must be greater than or equal to the threshold plus the lower bound). Otherwise, it is exclusive (the metric must be greater than the threshold plus the lower bound). A null value indicates negative infinity.</p>"""
    metric_interval_upper_bound: NotRequired[
        "capo_auto_scaling.types.metric_scale.MetricScale"
    ]
    """<p>The upper bound for the difference between the alarm threshold and the CloudWatch metric. If the metric value is above the breach threshold, the upper bound is exclusive (the metric must be less than the threshold plus the upper bound). Otherwise, it is inclusive (the metric must be less than or equal to the threshold plus the upper bound). A null value indicates positive infinity.</p> <p>The upper bound must be greater than the lower bound.</p>"""
    scaling_adjustment: NotRequired[
        "capo_auto_scaling.types.policy_increment.PolicyIncrement"
    ]
    """<p>The amount by which to scale, based on the specified adjustment type. A positive value adds to the current capacity while a negative number removes from the current capacity. For exact capacity, you must specify a non-negative value.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: StepAdjustment, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "metric_interval_lower_bound" in value:
        pairs.append(
            (
                f"{prefix}.MetricIntervalLowerBound",
                str(value["metric_interval_lower_bound"]),
            )
        )
    if "metric_interval_upper_bound" in value:
        pairs.append(
            (
                f"{prefix}.MetricIntervalUpperBound",
                str(value["metric_interval_upper_bound"]),
            )
        )
    if "scaling_adjustment" in value:
        pairs.append((f"{prefix}.ScalingAdjustment", str(value["scaling_adjustment"])))


def deserialize_query(el: Element) -> StepAdjustment:
    out: StepAdjustment = {}  # type: ignore[typeddict-item]
    child_metric_interval_lower_bound = el.find("MetricIntervalLowerBound")
    if child_metric_interval_lower_bound is not None:
        out["metric_interval_lower_bound"] = float(
            child_metric_interval_lower_bound.text or ""
        )
    child_metric_interval_upper_bound = el.find("MetricIntervalUpperBound")
    if child_metric_interval_upper_bound is not None:
        out["metric_interval_upper_bound"] = float(
            child_metric_interval_upper_bound.text or ""
        )
    child_scaling_adjustment = el.find("ScalingAdjustment")
    if child_scaling_adjustment is not None:
        out["scaling_adjustment"] = int(child_scaling_adjustment.text or "")
    return out
