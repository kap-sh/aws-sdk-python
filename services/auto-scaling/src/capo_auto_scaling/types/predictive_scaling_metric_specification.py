"""Generated from Smithy shape ``com.amazonaws.autoscaling#PredictiveScalingMetricSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.metric_scale
    import capo_auto_scaling.types.predictive_scaling_customized_capacity_metric
    import capo_auto_scaling.types.predictive_scaling_customized_load_metric
    import capo_auto_scaling.types.predictive_scaling_customized_scaling_metric
    import capo_auto_scaling.types.predictive_scaling_predefined_load_metric
    import capo_auto_scaling.types.predictive_scaling_predefined_metric_pair
    import capo_auto_scaling.types.predictive_scaling_predefined_scaling_metric


class PredictiveScalingMetricSpecification(TypedDict, closed=True):
    target_value: NotRequired["capo_auto_scaling.types.metric_scale.MetricScale"]
    """<p>Specifies the target utilization.</p> <note> <p>Some metrics are based on a count instead of a percentage, such as the request count for an Application Load Balancer or the number of messages in an SQS queue. If the scaling policy specifies one of these metrics, specify the target utilization as the optimal average request or message count per instance during any one-minute interval. </p> </note>"""
    predefined_metric_pair_specification: NotRequired[
        "capo_auto_scaling.types.predictive_scaling_predefined_metric_pair.PredictiveScalingPredefinedMetricPair"
    ]
    """<p>The predefined metric pair specification from which Amazon EC2 Auto Scaling determines the appropriate scaling metric and load metric to use.</p>"""
    predefined_scaling_metric_specification: NotRequired[
        "capo_auto_scaling.types.predictive_scaling_predefined_scaling_metric.PredictiveScalingPredefinedScalingMetric"
    ]
    """<p>The predefined scaling metric specification.</p>"""
    predefined_load_metric_specification: NotRequired[
        "capo_auto_scaling.types.predictive_scaling_predefined_load_metric.PredictiveScalingPredefinedLoadMetric"
    ]
    """<p>The predefined load metric specification.</p>"""
    customized_scaling_metric_specification: NotRequired[
        "capo_auto_scaling.types.predictive_scaling_customized_scaling_metric.PredictiveScalingCustomizedScalingMetric"
    ]
    """<p>The customized scaling metric specification.</p>"""
    customized_load_metric_specification: NotRequired[
        "capo_auto_scaling.types.predictive_scaling_customized_load_metric.PredictiveScalingCustomizedLoadMetric"
    ]
    """<p>The customized load metric specification.</p>"""
    customized_capacity_metric_specification: NotRequired[
        "capo_auto_scaling.types.predictive_scaling_customized_capacity_metric.PredictiveScalingCustomizedCapacityMetric"
    ]
    """<p>The customized capacity metric specification.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PredictiveScalingMetricSpecification,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "target_value" in value:
        pairs.append((f"{key_prefix}TargetValue", str(value["target_value"])))
    if "predefined_metric_pair_specification" in value:
        import capo_auto_scaling.types.predictive_scaling_predefined_metric_pair

        capo_auto_scaling.types.predictive_scaling_predefined_metric_pair.serialize_query(
            value["predefined_metric_pair_specification"],
            pairs,
            f"{key_prefix}PredefinedMetricPairSpecification",
        )
    if "predefined_scaling_metric_specification" in value:
        import capo_auto_scaling.types.predictive_scaling_predefined_scaling_metric

        capo_auto_scaling.types.predictive_scaling_predefined_scaling_metric.serialize_query(
            value["predefined_scaling_metric_specification"],
            pairs,
            f"{key_prefix}PredefinedScalingMetricSpecification",
        )
    if "predefined_load_metric_specification" in value:
        import capo_auto_scaling.types.predictive_scaling_predefined_load_metric

        capo_auto_scaling.types.predictive_scaling_predefined_load_metric.serialize_query(
            value["predefined_load_metric_specification"],
            pairs,
            f"{key_prefix}PredefinedLoadMetricSpecification",
        )
    if "customized_scaling_metric_specification" in value:
        import capo_auto_scaling.types.predictive_scaling_customized_scaling_metric

        capo_auto_scaling.types.predictive_scaling_customized_scaling_metric.serialize_query(
            value["customized_scaling_metric_specification"],
            pairs,
            f"{key_prefix}CustomizedScalingMetricSpecification",
        )
    if "customized_load_metric_specification" in value:
        import capo_auto_scaling.types.predictive_scaling_customized_load_metric

        capo_auto_scaling.types.predictive_scaling_customized_load_metric.serialize_query(
            value["customized_load_metric_specification"],
            pairs,
            f"{key_prefix}CustomizedLoadMetricSpecification",
        )
    if "customized_capacity_metric_specification" in value:
        import capo_auto_scaling.types.predictive_scaling_customized_capacity_metric

        capo_auto_scaling.types.predictive_scaling_customized_capacity_metric.serialize_query(
            value["customized_capacity_metric_specification"],
            pairs,
            f"{key_prefix}CustomizedCapacityMetricSpecification",
        )


def deserialize_query(el: Element) -> PredictiveScalingMetricSpecification:
    out: PredictiveScalingMetricSpecification = {}  # type: ignore[typeddict-item]
    child_target_value = el.find("TargetValue")
    if child_target_value is not None:
        out["target_value"] = float(child_target_value.text or "")
    child_predefined_metric_pair_specification = el.find(
        "PredefinedMetricPairSpecification"
    )
    if child_predefined_metric_pair_specification is not None:
        import capo_auto_scaling.types.predictive_scaling_predefined_metric_pair

        out["predefined_metric_pair_specification"] = (
            capo_auto_scaling.types.predictive_scaling_predefined_metric_pair.deserialize_query(
                child_predefined_metric_pair_specification
            )
        )
    child_predefined_scaling_metric_specification = el.find(
        "PredefinedScalingMetricSpecification"
    )
    if child_predefined_scaling_metric_specification is not None:
        import capo_auto_scaling.types.predictive_scaling_predefined_scaling_metric

        out["predefined_scaling_metric_specification"] = (
            capo_auto_scaling.types.predictive_scaling_predefined_scaling_metric.deserialize_query(
                child_predefined_scaling_metric_specification
            )
        )
    child_predefined_load_metric_specification = el.find(
        "PredefinedLoadMetricSpecification"
    )
    if child_predefined_load_metric_specification is not None:
        import capo_auto_scaling.types.predictive_scaling_predefined_load_metric

        out["predefined_load_metric_specification"] = (
            capo_auto_scaling.types.predictive_scaling_predefined_load_metric.deserialize_query(
                child_predefined_load_metric_specification
            )
        )
    child_customized_scaling_metric_specification = el.find(
        "CustomizedScalingMetricSpecification"
    )
    if child_customized_scaling_metric_specification is not None:
        import capo_auto_scaling.types.predictive_scaling_customized_scaling_metric

        out["customized_scaling_metric_specification"] = (
            capo_auto_scaling.types.predictive_scaling_customized_scaling_metric.deserialize_query(
                child_customized_scaling_metric_specification
            )
        )
    child_customized_load_metric_specification = el.find(
        "CustomizedLoadMetricSpecification"
    )
    if child_customized_load_metric_specification is not None:
        import capo_auto_scaling.types.predictive_scaling_customized_load_metric

        out["customized_load_metric_specification"] = (
            capo_auto_scaling.types.predictive_scaling_customized_load_metric.deserialize_query(
                child_customized_load_metric_specification
            )
        )
    child_customized_capacity_metric_specification = el.find(
        "CustomizedCapacityMetricSpecification"
    )
    if child_customized_capacity_metric_specification is not None:
        import capo_auto_scaling.types.predictive_scaling_customized_capacity_metric

        out["customized_capacity_metric_specification"] = (
            capo_auto_scaling.types.predictive_scaling_customized_capacity_metric.deserialize_query(
                child_customized_capacity_metric_specification
            )
        )
    return out
