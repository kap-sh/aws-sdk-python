"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#ModifyLoadBalancerAttributesOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing.types.access_point_name
    import aws_sdk_elastic_load_balancing.types.load_balancer_attributes


class ModifyLoadBalancerAttributesOutput(TypedDict):
    load_balancer_name: NotRequired[
        "aws_sdk_elastic_load_balancing.types.access_point_name.AccessPointName"
    ]
    """<p>The name of the load balancer.</p>"""
    load_balancer_attributes: NotRequired[
        "aws_sdk_elastic_load_balancing.types.load_balancer_attributes.LoadBalancerAttributes"
    ]
    """<p>Information about the load balancer attributes.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyLoadBalancerAttributesOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "load_balancer_name" in value:
        pairs.append((f"{prefix}.LoadBalancerName", str(value["load_balancer_name"])))
    if "load_balancer_attributes" in value:
        import aws_sdk_elastic_load_balancing.types.load_balancer_attributes

        aws_sdk_elastic_load_balancing.types.load_balancer_attributes.serialize_query(
            value["load_balancer_attributes"], pairs, f"{prefix}.LoadBalancerAttributes"
        )


def deserialize_query(el: Element) -> ModifyLoadBalancerAttributesOutput:
    out: ModifyLoadBalancerAttributesOutput = {}  # type: ignore[typeddict-item]
    child_load_balancer_name = el.find("LoadBalancerName")
    if child_load_balancer_name is not None:
        out["load_balancer_name"] = str(child_load_balancer_name.text or "")
    child_load_balancer_attributes = el.find("LoadBalancerAttributes")
    if child_load_balancer_attributes is not None:
        import aws_sdk_elastic_load_balancing.types.load_balancer_attributes

        out["load_balancer_attributes"] = (
            aws_sdk_elastic_load_balancing.types.load_balancer_attributes.deserialize_query(
                child_load_balancer_attributes
            )
        )
    return out
