"""Generated from Smithy shape ``com.amazonaws.autoscaling#DetachLoadBalancersType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.load_balancer_names
    import aws_sdk_auto_scaling.types.xml_string_max_len255


class DetachLoadBalancersType(TypedDict, closed=True):
    auto_scaling_group_name: NotRequired[
        "aws_sdk_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The name of the Auto Scaling group.</p>"""
    load_balancer_names: NotRequired[
        "aws_sdk_auto_scaling.types.load_balancer_names.LoadBalancerNames"
    ]
    """<p>The names of the load balancers. You can specify up to 10 load balancers.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DetachLoadBalancersType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "auto_scaling_group_name" in value:
        pairs.append(
            (f"{prefix}.AutoScalingGroupName", str(value["auto_scaling_group_name"]))
        )
    if "load_balancer_names" in value:
        import aws_sdk_auto_scaling.types.load_balancer_names

        aws_sdk_auto_scaling.types.load_balancer_names.serialize_query(
            value["load_balancer_names"], pairs, f"{prefix}.LoadBalancerNames"
        )


def deserialize_query(el: Element) -> DetachLoadBalancersType:
    out: DetachLoadBalancersType = {}  # type: ignore[typeddict-item]
    child_auto_scaling_group_name = el.find("AutoScalingGroupName")
    if child_auto_scaling_group_name is not None:
        out["auto_scaling_group_name"] = str(child_auto_scaling_group_name.text or "")
    child_load_balancer_names = el.find("LoadBalancerNames")
    if child_load_balancer_names is not None:
        import aws_sdk_auto_scaling.types.load_balancer_names

        out["load_balancer_names"] = (
            aws_sdk_auto_scaling.types.load_balancer_names.deserialize_query(
                child_load_balancer_names
            )
        )
    return out
