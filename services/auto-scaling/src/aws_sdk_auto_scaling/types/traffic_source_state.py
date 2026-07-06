"""Generated from Smithy shape ``com.amazonaws.autoscaling#TrafficSourceState``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.xml_string_max_len255
    import aws_sdk_auto_scaling.types.xml_string_max_len511


class TrafficSourceState(TypedDict, closed=True):
    traffic_source: NotRequired[
        "aws_sdk_auto_scaling.types.xml_string_max_len511.XmlStringMaxLen511"
    ]
    """<p>This is replaced by <code>Identifier</code>.</p>"""
    state: NotRequired[
        "aws_sdk_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>Describes the current state of a traffic source.</p> <p>The state values are as follows:</p> <ul> <li> <p> <code>Adding</code> - The Auto Scaling instances are being registered with the load balancer or target group.</p> </li> <li> <p> <code>Added</code> - All Auto Scaling instances are registered with the load balancer or target group.</p> </li> <li> <p> <code>InService</code> - For an Elastic Load Balancing load balancer or target group, at least one Auto Scaling instance passed an <code>ELB</code> health check. For VPC Lattice, at least one Auto Scaling instance passed an <code>VPC_LATTICE</code> health check.</p> </li> <li> <p> <code>Removing</code> - The Auto Scaling instances are being deregistered from the load balancer or target group. If connection draining (deregistration delay) is enabled, Elastic Load Balancing or VPC Lattice waits for in-flight requests to complete before deregistering the instances.</p> </li> <li> <p> <code>Removed</code> - All Auto Scaling instances are deregistered from the load balancer or target group.</p> </li> </ul>"""
    identifier: NotRequired[
        "aws_sdk_auto_scaling.types.xml_string_max_len511.XmlStringMaxLen511"
    ]
    """<p>The unique identifier of the traffic source.</p>"""
    type: NotRequired[
        "aws_sdk_auto_scaling.types.xml_string_max_len511.XmlStringMaxLen511"
    ]
    """<p>Provides additional context for the value of <code>Identifier</code>.</p> <p>The following lists the valid values:</p> <ul> <li> <p> <code>elb</code> if <code>Identifier</code> is the name of a Classic Load Balancer.</p> </li> <li> <p> <code>elbv2</code> if <code>Identifier</code> is the ARN of an Application Load Balancer, Gateway Load Balancer, or Network Load Balancer target group.</p> </li> <li> <p> <code>vpc-lattice</code> if <code>Identifier</code> is the ARN of a VPC Lattice target group.</p> </li> </ul> <p>Required if the identifier is the name of a Classic Load Balancer.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: TrafficSourceState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "traffic_source" in value:
        pairs.append((f"{prefix}.TrafficSource", str(value["traffic_source"])))
    if "state" in value:
        pairs.append((f"{prefix}.State", str(value["state"])))
    if "identifier" in value:
        pairs.append((f"{prefix}.Identifier", str(value["identifier"])))
    if "type" in value:
        pairs.append((f"{prefix}.Type", str(value["type"])))


def deserialize_query(el: Element) -> TrafficSourceState:
    out: TrafficSourceState = {}  # type: ignore[typeddict-item]
    child_traffic_source = el.find("TrafficSource")
    if child_traffic_source is not None:
        out["traffic_source"] = str(child_traffic_source.text or "")
    child_state = el.find("State")
    if child_state is not None:
        out["state"] = str(child_state.text or "")
    child_identifier = el.find("Identifier")
    if child_identifier is not None:
        out["identifier"] = str(child_identifier.text or "")
    child_type = el.find("Type")
    if child_type is not None:
        out["type"] = str(child_type.text or "")
    return out
