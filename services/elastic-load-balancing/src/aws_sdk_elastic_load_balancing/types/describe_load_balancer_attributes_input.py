"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#DescribeLoadBalancerAttributesInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_elastic_load_balancing._protocol.xml import Element
from aws_sdk_elastic_load_balancing.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing.types.access_point_name


class DescribeLoadBalancerAttributesInput(TypedDict):
    load_balancer_name: (
        "aws_sdk_elastic_load_balancing.types.access_point_name.AccessPointName"
    )
    """<p>The name of the load balancer.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeLoadBalancerAttributesInput,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((f"{prefix}.LoadBalancerName", str(value["load_balancer_name"])))


def deserialize_query(el: Element) -> DescribeLoadBalancerAttributesInput:
    out: DescribeLoadBalancerAttributesInput = {}  # type: ignore[typeddict-item]
    child_load_balancer_name = el.find("LoadBalancerName")
    if child_load_balancer_name is not None:
        out["load_balancer_name"] = str(child_load_balancer_name.text or "")
    else:
        raise DeserializationError(
            "DescribeLoadBalancerAttributesInput.load_balancer_name required"
        )
    return out
