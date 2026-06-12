"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#LoadBalancerAddresses``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.load_balancer_address

LoadBalancerAddresses: TypeAlias = list[
    "aws_sdk_elastic_load_balancing_v2.types.load_balancer_address.LoadBalancerAddress"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: LoadBalancerAddresses, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elastic_load_balancing_v2.types.load_balancer_address

    for n, item in enumerate(value, 1):
        aws_sdk_elastic_load_balancing_v2.types.load_balancer_address.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> LoadBalancerAddresses:
    import aws_sdk_elastic_load_balancing_v2.types.load_balancer_address

    out: LoadBalancerAddresses = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_elastic_load_balancing_v2.types.load_balancer_address.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: LoadBalancerAddresses, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elastic_load_balancing_v2.types.load_balancer_address

    for n, item in enumerate(value, 1):
        aws_sdk_elastic_load_balancing_v2.types.load_balancer_address.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> LoadBalancerAddresses:
    import aws_sdk_elastic_load_balancing_v2.types.load_balancer_address

    out: LoadBalancerAddresses = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_elastic_load_balancing_v2.types.load_balancer_address.deserialize_query(
                child
            )
        )
    return out
