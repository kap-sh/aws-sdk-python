"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#DescribeLoadBalancerAttributesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing.types.load_balancer_attributes


class DescribeLoadBalancerAttributesOutput(TypedDict, closed=True):
    load_balancer_attributes: NotRequired[
        "aws_sdk_elastic_load_balancing.types.load_balancer_attributes.LoadBalancerAttributes"
    ]
    """<p>Information about the load balancer attributes.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeLoadBalancerAttributesOutput,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "load_balancer_attributes" in value:
        import aws_sdk_elastic_load_balancing.types.load_balancer_attributes

        aws_sdk_elastic_load_balancing.types.load_balancer_attributes.serialize_query(
            value["load_balancer_attributes"], pairs, f"{prefix}.LoadBalancerAttributes"
        )


def deserialize_query(el: Element) -> DescribeLoadBalancerAttributesOutput:
    out: DescribeLoadBalancerAttributesOutput = {}  # type: ignore[typeddict-item]
    child_load_balancer_attributes = el.find("LoadBalancerAttributes")
    if child_load_balancer_attributes is not None:
        import aws_sdk_elastic_load_balancing.types.load_balancer_attributes

        out["load_balancer_attributes"] = (
            aws_sdk_elastic_load_balancing.types.load_balancer_attributes.deserialize_query(
                child_load_balancer_attributes
            )
        )
    return out
