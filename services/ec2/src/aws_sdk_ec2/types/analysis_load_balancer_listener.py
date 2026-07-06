"""Generated from Smithy shape ``com.amazonaws.ec2#AnalysisLoadBalancerListener``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.port


class AnalysisLoadBalancerListener(TypedDict, closed=True):
    load_balancer_port: NotRequired["aws_sdk_ec2.types.port.Port"]
    """<p>The port on which the load balancer is listening.</p>"""
    instance_port: NotRequired["aws_sdk_ec2.types.port.Port"]
    """<p>[Classic Load Balancers] The back-end port for the listener.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AnalysisLoadBalancerListener, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "load_balancer_port" in value:
        pairs.append((f"{prefix}.LoadBalancerPort", str(value["load_balancer_port"])))
    if "instance_port" in value:
        pairs.append((f"{prefix}.InstancePort", str(value["instance_port"])))


def deserialize_ec2_query(el: Element) -> AnalysisLoadBalancerListener:
    out: AnalysisLoadBalancerListener = {}  # type: ignore[typeddict-item]
    child_load_balancer_port = el.find("LoadBalancerPort")
    if child_load_balancer_port is not None:
        out["load_balancer_port"] = int(child_load_balancer_port.text or "")
    child_instance_port = el.find("InstancePort")
    if child_instance_port is not None:
        out["instance_port"] = int(child_instance_port.text or "")
    return out
