"""Generated from Smithy shape ``com.amazonaws.autoscaling#TargetTrackingConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.customized_metric_specification
    import aws_sdk_auto_scaling.types.disable_scale_in
    import aws_sdk_auto_scaling.types.metric_scale
    import aws_sdk_auto_scaling.types.predefined_metric_specification


class TargetTrackingConfiguration(TypedDict):
    predefined_metric_specification: NotRequired[
        "aws_sdk_auto_scaling.types.predefined_metric_specification.PredefinedMetricSpecification"
    ]
    """<p>A predefined metric. You must specify either a predefined metric or a customized metric.</p>"""
    customized_metric_specification: NotRequired[
        "aws_sdk_auto_scaling.types.customized_metric_specification.CustomizedMetricSpecification"
    ]
    """<p>A customized metric. You must specify either a predefined metric or a customized metric.</p>"""
    target_value: NotRequired["aws_sdk_auto_scaling.types.metric_scale.MetricScale"]
    """<p>The target value for the metric.</p> <note> <p>Some metrics are based on a count instead of a percentage, such as the request count for an Application Load Balancer or the number of messages in an SQS queue. If the scaling policy specifies one of these metrics, specify the target utilization as the optimal average request or message count per instance during any one-minute interval. </p> </note>"""
    disable_scale_in: NotRequired[
        "aws_sdk_auto_scaling.types.disable_scale_in.DisableScaleIn"
    ]
    """<p>Indicates whether scaling in by the target tracking scaling policy is disabled. If scaling in is disabled, the target tracking scaling policy doesn't remove instances from the Auto Scaling group. Otherwise, the target tracking scaling policy can remove instances from the Auto Scaling group. The default is <code>false</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: TargetTrackingConfiguration, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "predefined_metric_specification" in value:
        import aws_sdk_auto_scaling.types.predefined_metric_specification

        aws_sdk_auto_scaling.types.predefined_metric_specification.serialize_query(
            value["predefined_metric_specification"],
            pairs,
            f"{prefix}.PredefinedMetricSpecification",
        )
    if "customized_metric_specification" in value:
        import aws_sdk_auto_scaling.types.customized_metric_specification

        aws_sdk_auto_scaling.types.customized_metric_specification.serialize_query(
            value["customized_metric_specification"],
            pairs,
            f"{prefix}.CustomizedMetricSpecification",
        )
    if "target_value" in value:
        pairs.append((f"{prefix}.TargetValue", str(value["target_value"])))
    if "disable_scale_in" in value:
        pairs.append(
            (
                f"{prefix}.DisableScaleIn",
                "true" if value["disable_scale_in"] else "false",
            )
        )


def deserialize_query(el: Element) -> TargetTrackingConfiguration:
    out: TargetTrackingConfiguration = {}  # type: ignore[typeddict-item]
    child_predefined_metric_specification = el.find("PredefinedMetricSpecification")
    if child_predefined_metric_specification is not None:
        import aws_sdk_auto_scaling.types.predefined_metric_specification

        out["predefined_metric_specification"] = (
            aws_sdk_auto_scaling.types.predefined_metric_specification.deserialize_query(
                child_predefined_metric_specification
            )
        )
    child_customized_metric_specification = el.find("CustomizedMetricSpecification")
    if child_customized_metric_specification is not None:
        import aws_sdk_auto_scaling.types.customized_metric_specification

        out["customized_metric_specification"] = (
            aws_sdk_auto_scaling.types.customized_metric_specification.deserialize_query(
                child_customized_metric_specification
            )
        )
    child_target_value = el.find("TargetValue")
    if child_target_value is not None:
        out["target_value"] = float(child_target_value.text or "")
    child_disable_scale_in = el.find("DisableScaleIn")
    if child_disable_scale_in is not None:
        out["disable_scale_in"] = (child_disable_scale_in.text or "").lower() == "true"
    return out
