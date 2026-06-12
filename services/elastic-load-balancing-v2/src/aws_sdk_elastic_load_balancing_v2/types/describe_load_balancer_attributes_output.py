"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#DescribeLoadBalancerAttributesOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.load_balancer_attributes


class DescribeLoadBalancerAttributesOutput(TypedDict):
    attributes: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.load_balancer_attributes.LoadBalancerAttributes"
    ]
    """<p>Information about the load balancer attributes.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeLoadBalancerAttributesOutput,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "attributes" in value:
        import aws_sdk_elastic_load_balancing_v2.types.load_balancer_attributes

        aws_sdk_elastic_load_balancing_v2.types.load_balancer_attributes.serialize_query(
            value["attributes"], pairs, f"{prefix}.Attributes"
        )


def deserialize_query(el: Element) -> DescribeLoadBalancerAttributesOutput:
    out: DescribeLoadBalancerAttributesOutput = {}  # type: ignore[typeddict-item]
    child_attributes = el.find("Attributes")
    if child_attributes is not None:
        import aws_sdk_elastic_load_balancing_v2.types.load_balancer_attributes

        out["attributes"] = (
            aws_sdk_elastic_load_balancing_v2.types.load_balancer_attributes.deserialize_query(
                child_attributes
            )
        )
    return out
