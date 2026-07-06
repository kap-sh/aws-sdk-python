"""Generated from Smithy shape ``com.amazonaws.autoscaling#DetachLoadBalancerTargetGroupsType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.target_group_ar_ns
    import aws_sdk_auto_scaling.types.xml_string_max_len255


class DetachLoadBalancerTargetGroupsType(TypedDict, closed=True):
    auto_scaling_group_name: NotRequired[
        "aws_sdk_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The name of the Auto Scaling group.</p>"""
    target_group_ar_ns: NotRequired[
        "aws_sdk_auto_scaling.types.target_group_ar_ns.TargetGroupARNs"
    ]
    """<p>The Amazon Resource Names (ARN) of the target groups. You can specify up to 10 target groups.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DetachLoadBalancerTargetGroupsType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "auto_scaling_group_name" in value:
        pairs.append(
            (f"{prefix}.AutoScalingGroupName", str(value["auto_scaling_group_name"]))
        )
    if "target_group_ar_ns" in value:
        import aws_sdk_auto_scaling.types.target_group_ar_ns

        aws_sdk_auto_scaling.types.target_group_ar_ns.serialize_query(
            value["target_group_ar_ns"], pairs, f"{prefix}.TargetGroupARNs"
        )


def deserialize_query(el: Element) -> DetachLoadBalancerTargetGroupsType:
    out: DetachLoadBalancerTargetGroupsType = {}  # type: ignore[typeddict-item]
    child_auto_scaling_group_name = el.find("AutoScalingGroupName")
    if child_auto_scaling_group_name is not None:
        out["auto_scaling_group_name"] = str(child_auto_scaling_group_name.text or "")
    child_target_group_ar_ns = el.find("TargetGroupARNs")
    if child_target_group_ar_ns is not None:
        import aws_sdk_auto_scaling.types.target_group_ar_ns

        out["target_group_ar_ns"] = (
            aws_sdk_auto_scaling.types.target_group_ar_ns.deserialize_query(
                child_target_group_ar_ns
            )
        )
    return out
