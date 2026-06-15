"""Generated from Smithy shape ``com.amazonaws.autoscaling#PutScalingPolicyType``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.cooldown
    import aws_sdk_auto_scaling.types.estimated_instance_warmup
    import aws_sdk_auto_scaling.types.min_adjustment_magnitude
    import aws_sdk_auto_scaling.types.min_adjustment_step
    import aws_sdk_auto_scaling.types.policy_increment
    import aws_sdk_auto_scaling.types.predictive_scaling_configuration
    import aws_sdk_auto_scaling.types.scaling_policy_enabled
    import aws_sdk_auto_scaling.types.step_adjustments
    import aws_sdk_auto_scaling.types.target_tracking_configuration
    import aws_sdk_auto_scaling.types.xml_string_max_len32
    import aws_sdk_auto_scaling.types.xml_string_max_len64
    import aws_sdk_auto_scaling.types.xml_string_max_len255


class PutScalingPolicyType(TypedDict):
    auto_scaling_group_name: NotRequired[
        "aws_sdk_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The name of the Auto Scaling group.</p>"""
    policy_name: NotRequired[
        "aws_sdk_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The name of the policy.</p>"""
    policy_type: NotRequired[
        "aws_sdk_auto_scaling.types.xml_string_max_len64.XmlStringMaxLen64"
    ]
    """<p>One of the following policy types: </p> <ul> <li> <p> <code>TargetTrackingScaling</code> </p> </li> <li> <p> <code>StepScaling</code> </p> </li> <li> <p> <code>SimpleScaling</code> (default)</p> </li> <li> <p> <code>PredictiveScaling</code> </p> </li> </ul>"""
    adjustment_type: NotRequired[
        "aws_sdk_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    r"""<p>Specifies how the scaling adjustment is interpreted (for example, an absolute number or a percentage). The valid values are <code>ChangeInCapacity</code>, <code>ExactCapacity</code>, and <code>PercentChangeInCapacity</code>.</p> <p>Required if the policy type is <code>StepScaling</code> or <code>SimpleScaling</code>. For more information, see <a href=\"https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-simple-step.html#as-scaling-adjustment\">Scaling adjustment types</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>"""
    min_adjustment_step: NotRequired[
        "aws_sdk_auto_scaling.types.min_adjustment_step.MinAdjustmentStep"
    ]
    """<p>Available for backward compatibility. Use <code>MinAdjustmentMagnitude</code> instead.</p>"""
    min_adjustment_magnitude: NotRequired[
        "aws_sdk_auto_scaling.types.min_adjustment_magnitude.MinAdjustmentMagnitude"
    ]
    r"""<p>The minimum value to scale by when the adjustment type is <code>PercentChangeInCapacity</code>. For example, suppose that you create a step scaling policy to scale out an Auto Scaling group by 25 percent and you specify a <code>MinAdjustmentMagnitude</code> of 2. If the group has 4 instances and the scaling policy is performed, 25 percent of 4 is 1. However, because you specified a <code>MinAdjustmentMagnitude</code> of 2, Amazon EC2 Auto Scaling scales out the group by 2 instances.</p> <p>Valid only if the policy type is <code>StepScaling</code> or <code>SimpleScaling</code>. For more information, see <a href=\"https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-simple-step.html#as-scaling-adjustment\">Scaling adjustment types</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p> <note> <p>Some Auto Scaling groups use instance weights. In this case, set the <code>MinAdjustmentMagnitude</code> to a value that is at least as large as your largest instance weight.</p> </note>"""
    scaling_adjustment: NotRequired[
        "aws_sdk_auto_scaling.types.policy_increment.PolicyIncrement"
    ]
    """<p>The amount by which to scale, based on the specified adjustment type. A positive value adds to the current capacity while a negative number removes from the current capacity. For exact capacity, you must specify a non-negative value.</p> <p>Required if the policy type is <code>SimpleScaling</code>. (Not used with any other policy type.) </p>"""
    cooldown: NotRequired["aws_sdk_auto_scaling.types.cooldown.Cooldown"]
    r"""<p>A cooldown period, in seconds, that applies to a specific simple scaling policy. When a cooldown period is specified here, it overrides the default cooldown.</p> <p>Valid only if the policy type is <code>SimpleScaling</code>. For more information, see <a href=\"https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-scaling-cooldowns.html\">Scaling cooldowns for Amazon EC2 Auto Scaling</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p> <p>Default: None</p>"""
    metric_aggregation_type: NotRequired[
        "aws_sdk_auto_scaling.types.xml_string_max_len32.XmlStringMaxLen32"
    ]
    """<p>The aggregation type for the CloudWatch metrics. The valid values are <code>Minimum</code>, <code>Maximum</code>, and <code>Average</code>. If the aggregation type is null, the value is treated as <code>Average</code>.</p> <p>Valid only if the policy type is <code>StepScaling</code>.</p>"""
    step_adjustments: NotRequired[
        "aws_sdk_auto_scaling.types.step_adjustments.StepAdjustments"
    ]
    """<p>A set of adjustments that enable you to scale based on the size of the alarm breach.</p> <p>Required if the policy type is <code>StepScaling</code>. (Not used with any other policy type.) </p>"""
    estimated_instance_warmup: NotRequired[
        "aws_sdk_auto_scaling.types.estimated_instance_warmup.EstimatedInstanceWarmup"
    ]
    """<p> <i>Not needed if the default instance warmup is defined for the group.</i> </p> <p>The estimated time, in seconds, until a newly launched instance can contribute to the CloudWatch metrics. This warm-up period applies to instances launched due to a specific target tracking or step scaling policy. When a warm-up period is specified here, it overrides the default instance warmup.</p> <p>Valid only if the policy type is <code>TargetTrackingScaling</code> or <code>StepScaling</code>.</p> <note> <p>The default is to use the value for the default instance warmup defined for the group. If default instance warmup is null, then <code>EstimatedInstanceWarmup</code> falls back to the value of default cooldown.</p> </note>"""
    target_tracking_configuration: NotRequired[
        "aws_sdk_auto_scaling.types.target_tracking_configuration.TargetTrackingConfiguration"
    ]
    r"""<p>A target tracking scaling policy. Provides support for predefined or custom metrics.</p> <p>The following predefined metrics are available:</p> <ul> <li> <p> <code>ASGAverageCPUUtilization</code> </p> </li> <li> <p> <code>ASGAverageNetworkIn</code> </p> </li> <li> <p> <code>ASGAverageNetworkOut</code> </p> </li> <li> <p> <code>ALBRequestCountPerTarget</code> </p> </li> </ul> <p>If you specify <code>ALBRequestCountPerTarget</code> for the metric, you must specify the <code>ResourceLabel</code> property with the <code>PredefinedMetricSpecification</code>.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_TargetTrackingConfiguration.html\">TargetTrackingConfiguration</a> in the <i>Amazon EC2 Auto Scaling API Reference</i>.</p> <p>Required if the policy type is <code>TargetTrackingScaling</code>.</p>"""
    enabled: NotRequired[
        "aws_sdk_auto_scaling.types.scaling_policy_enabled.ScalingPolicyEnabled"
    ]
    r"""<p>Indicates whether the scaling policy is enabled or disabled. The default is enabled. For more information, see <a href=\"https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-enable-disable-scaling-policy.html\">Disable a scaling policy for an Auto Scaling group</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>"""
    predictive_scaling_configuration: NotRequired[
        "aws_sdk_auto_scaling.types.predictive_scaling_configuration.PredictiveScalingConfiguration"
    ]
    r"""<p>A predictive scaling policy. Provides support for predefined and custom metrics.</p> <p>Predefined metrics include CPU utilization, network in/out, and the Application Load Balancer request count.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_PredictiveScalingConfiguration.html\">PredictiveScalingConfiguration</a> in the <i>Amazon EC2 Auto Scaling API Reference</i>.</p> <p>Required if the policy type is <code>PredictiveScaling</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PutScalingPolicyType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "auto_scaling_group_name" in value:
        pairs.append(
            (f"{prefix}.AutoScalingGroupName", str(value["auto_scaling_group_name"]))
        )
    if "policy_name" in value:
        pairs.append((f"{prefix}.PolicyName", str(value["policy_name"])))
    if "policy_type" in value:
        pairs.append((f"{prefix}.PolicyType", str(value["policy_type"])))
    if "adjustment_type" in value:
        pairs.append((f"{prefix}.AdjustmentType", str(value["adjustment_type"])))
    if "min_adjustment_step" in value:
        pairs.append((f"{prefix}.MinAdjustmentStep", str(value["min_adjustment_step"])))
    if "min_adjustment_magnitude" in value:
        pairs.append(
            (f"{prefix}.MinAdjustmentMagnitude", str(value["min_adjustment_magnitude"]))
        )
    if "scaling_adjustment" in value:
        pairs.append((f"{prefix}.ScalingAdjustment", str(value["scaling_adjustment"])))
    if "cooldown" in value:
        pairs.append((f"{prefix}.Cooldown", str(value["cooldown"])))
    if "metric_aggregation_type" in value:
        pairs.append(
            (f"{prefix}.MetricAggregationType", str(value["metric_aggregation_type"]))
        )
    if "step_adjustments" in value:
        import aws_sdk_auto_scaling.types.step_adjustments

        aws_sdk_auto_scaling.types.step_adjustments.serialize_query(
            value["step_adjustments"], pairs, f"{prefix}.StepAdjustments"
        )
    if "estimated_instance_warmup" in value:
        pairs.append(
            (
                f"{prefix}.EstimatedInstanceWarmup",
                str(value["estimated_instance_warmup"]),
            )
        )
    if "target_tracking_configuration" in value:
        import aws_sdk_auto_scaling.types.target_tracking_configuration

        aws_sdk_auto_scaling.types.target_tracking_configuration.serialize_query(
            value["target_tracking_configuration"],
            pairs,
            f"{prefix}.TargetTrackingConfiguration",
        )
    if "enabled" in value:
        pairs.append((f"{prefix}.Enabled", "true" if value["enabled"] else "false"))
    if "predictive_scaling_configuration" in value:
        import aws_sdk_auto_scaling.types.predictive_scaling_configuration

        aws_sdk_auto_scaling.types.predictive_scaling_configuration.serialize_query(
            value["predictive_scaling_configuration"],
            pairs,
            f"{prefix}.PredictiveScalingConfiguration",
        )


def deserialize_query(el: Element) -> PutScalingPolicyType:
    out: PutScalingPolicyType = {}  # type: ignore[typeddict-item]
    child_auto_scaling_group_name = el.find("AutoScalingGroupName")
    if child_auto_scaling_group_name is not None:
        out["auto_scaling_group_name"] = str(child_auto_scaling_group_name.text or "")
    child_policy_name = el.find("PolicyName")
    if child_policy_name is not None:
        out["policy_name"] = str(child_policy_name.text or "")
    child_policy_type = el.find("PolicyType")
    if child_policy_type is not None:
        out["policy_type"] = str(child_policy_type.text or "")
    child_adjustment_type = el.find("AdjustmentType")
    if child_adjustment_type is not None:
        out["adjustment_type"] = str(child_adjustment_type.text or "")
    child_min_adjustment_step = el.find("MinAdjustmentStep")
    if child_min_adjustment_step is not None:
        out["min_adjustment_step"] = int(child_min_adjustment_step.text or "")
    child_min_adjustment_magnitude = el.find("MinAdjustmentMagnitude")
    if child_min_adjustment_magnitude is not None:
        out["min_adjustment_magnitude"] = int(child_min_adjustment_magnitude.text or "")
    child_scaling_adjustment = el.find("ScalingAdjustment")
    if child_scaling_adjustment is not None:
        out["scaling_adjustment"] = int(child_scaling_adjustment.text or "")
    child_cooldown = el.find("Cooldown")
    if child_cooldown is not None:
        out["cooldown"] = int(child_cooldown.text or "")
    child_metric_aggregation_type = el.find("MetricAggregationType")
    if child_metric_aggregation_type is not None:
        out["metric_aggregation_type"] = str(child_metric_aggregation_type.text or "")
    child_step_adjustments = el.find("StepAdjustments")
    if child_step_adjustments is not None:
        import aws_sdk_auto_scaling.types.step_adjustments

        out["step_adjustments"] = (
            aws_sdk_auto_scaling.types.step_adjustments.deserialize_query(
                child_step_adjustments
            )
        )
    child_estimated_instance_warmup = el.find("EstimatedInstanceWarmup")
    if child_estimated_instance_warmup is not None:
        out["estimated_instance_warmup"] = int(
            child_estimated_instance_warmup.text or ""
        )
    child_target_tracking_configuration = el.find("TargetTrackingConfiguration")
    if child_target_tracking_configuration is not None:
        import aws_sdk_auto_scaling.types.target_tracking_configuration

        out["target_tracking_configuration"] = (
            aws_sdk_auto_scaling.types.target_tracking_configuration.deserialize_query(
                child_target_tracking_configuration
            )
        )
    child_enabled = el.find("Enabled")
    if child_enabled is not None:
        out["enabled"] = (child_enabled.text or "").lower() == "true"
    child_predictive_scaling_configuration = el.find("PredictiveScalingConfiguration")
    if child_predictive_scaling_configuration is not None:
        import aws_sdk_auto_scaling.types.predictive_scaling_configuration

        out["predictive_scaling_configuration"] = (
            aws_sdk_auto_scaling.types.predictive_scaling_configuration.deserialize_query(
                child_predictive_scaling_configuration
            )
        )
    return out
