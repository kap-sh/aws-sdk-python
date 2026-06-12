"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#LoadBalancerList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.load_balancer

LoadBalancerList: TypeAlias = list[
    "aws_sdk_elastic_beanstalk.types.load_balancer.LoadBalancer"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: LoadBalancerList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elastic_beanstalk.types.load_balancer

    for n, item in enumerate(value, 1):
        aws_sdk_elastic_beanstalk.types.load_balancer.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> LoadBalancerList:
    import aws_sdk_elastic_beanstalk.types.load_balancer

    out: LoadBalancerList = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_elastic_beanstalk.types.load_balancer.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: LoadBalancerList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elastic_beanstalk.types.load_balancer

    for n, item in enumerate(value, 1):
        aws_sdk_elastic_beanstalk.types.load_balancer.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> LoadBalancerList:
    import aws_sdk_elastic_beanstalk.types.load_balancer

    out: LoadBalancerList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_elastic_beanstalk.types.load_balancer.deserialize_query(child)
        )
    return out
