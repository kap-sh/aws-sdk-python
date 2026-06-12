"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#AttachLoadBalancerToSubnetsInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_elastic_load_balancing._protocol.xml import Element
from aws_sdk_elastic_load_balancing.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing.types.access_point_name
    import aws_sdk_elastic_load_balancing.types.subnets


class AttachLoadBalancerToSubnetsInput(TypedDict):
    load_balancer_name: (
        "aws_sdk_elastic_load_balancing.types.access_point_name.AccessPointName"
    )
    """<p>The name of the load balancer.</p>"""
    subnets: "aws_sdk_elastic_load_balancing.types.subnets.Subnets"
    """<p>The IDs of the subnets to add. You can add only one subnet per Availability Zone.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AttachLoadBalancerToSubnetsInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.LoadBalancerName", str(value["load_balancer_name"])))
    import aws_sdk_elastic_load_balancing.types.subnets

    aws_sdk_elastic_load_balancing.types.subnets.serialize_query(
        value["subnets"], pairs, f"{prefix}.Subnets"
    )


def deserialize_query(el: Element) -> AttachLoadBalancerToSubnetsInput:
    out: AttachLoadBalancerToSubnetsInput = {}  # type: ignore[typeddict-item]
    child_load_balancer_name = el.find("LoadBalancerName")
    if child_load_balancer_name is not None:
        out["load_balancer_name"] = str(child_load_balancer_name.text or "")
    else:
        raise DeserializationError(
            "AttachLoadBalancerToSubnetsInput.load_balancer_name required"
        )
    child_subnets = el.find("Subnets")
    if child_subnets is not None:
        import aws_sdk_elastic_load_balancing.types.subnets

        out["subnets"] = aws_sdk_elastic_load_balancing.types.subnets.deserialize_query(
            child_subnets
        )
    else:
        raise DeserializationError("AttachLoadBalancerToSubnetsInput.subnets required")
    return out
