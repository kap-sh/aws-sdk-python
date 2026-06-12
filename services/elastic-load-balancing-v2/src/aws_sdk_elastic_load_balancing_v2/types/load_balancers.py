"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#LoadBalancers``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.load_balancer

LoadBalancers: TypeAlias = list[
    "aws_sdk_elastic_load_balancing_v2.types.load_balancer.LoadBalancer"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: LoadBalancers, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elastic_load_balancing_v2.types.load_balancer

    for n, item in enumerate(value, 1):
        aws_sdk_elastic_load_balancing_v2.types.load_balancer.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> LoadBalancers:
    import aws_sdk_elastic_load_balancing_v2.types.load_balancer

    out: LoadBalancers = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_elastic_load_balancing_v2.types.load_balancer.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: LoadBalancers, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elastic_load_balancing_v2.types.load_balancer

    for n, item in enumerate(value, 1):
        aws_sdk_elastic_load_balancing_v2.types.load_balancer.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> LoadBalancers:
    import aws_sdk_elastic_load_balancing_v2.types.load_balancer

    out: LoadBalancers = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_elastic_load_balancing_v2.types.load_balancer.deserialize_query(
                child
            )
        )
    return out
