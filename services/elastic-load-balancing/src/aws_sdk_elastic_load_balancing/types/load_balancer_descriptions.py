"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#LoadBalancerDescriptions``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing.types.load_balancer_description

LoadBalancerDescriptions: TypeAlias = list[
    "aws_sdk_elastic_load_balancing.types.load_balancer_description.LoadBalancerDescription"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: LoadBalancerDescriptions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elastic_load_balancing.types.load_balancer_description

    for n, item in enumerate(value, 1):
        aws_sdk_elastic_load_balancing.types.load_balancer_description.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> LoadBalancerDescriptions:
    import aws_sdk_elastic_load_balancing.types.load_balancer_description

    out: LoadBalancerDescriptions = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_elastic_load_balancing.types.load_balancer_description.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: LoadBalancerDescriptions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elastic_load_balancing.types.load_balancer_description

    for n, item in enumerate(value, 1):
        aws_sdk_elastic_load_balancing.types.load_balancer_description.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> LoadBalancerDescriptions:
    import aws_sdk_elastic_load_balancing.types.load_balancer_description

    out: LoadBalancerDescriptions = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_elastic_load_balancing.types.load_balancer_description.deserialize_query(
                child
            )
        )
    return out
