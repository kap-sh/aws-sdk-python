"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#LoadBalancerAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.load_balancer_attribute

LoadBalancerAttributes: TypeAlias = list[
    "aws_sdk_elastic_load_balancing_v2.types.load_balancer_attribute.LoadBalancerAttribute"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: LoadBalancerAttributes, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elastic_load_balancing_v2.types.load_balancer_attribute

    for n, item in enumerate(value, 1):
        aws_sdk_elastic_load_balancing_v2.types.load_balancer_attribute.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> LoadBalancerAttributes:
    import aws_sdk_elastic_load_balancing_v2.types.load_balancer_attribute

    out: LoadBalancerAttributes = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_elastic_load_balancing_v2.types.load_balancer_attribute.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: LoadBalancerAttributes, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elastic_load_balancing_v2.types.load_balancer_attribute

    for n, item in enumerate(value, 1):
        aws_sdk_elastic_load_balancing_v2.types.load_balancer_attribute.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> LoadBalancerAttributes:
    import aws_sdk_elastic_load_balancing_v2.types.load_balancer_attribute

    out: LoadBalancerAttributes = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_elastic_load_balancing_v2.types.load_balancer_attribute.deserialize_query(
                child
            )
        )
    return out
