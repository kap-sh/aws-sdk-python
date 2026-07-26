"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#LoadBalancerListenersDescription``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.listener

LoadBalancerListenersDescription: TypeAlias = list[
    "capo_elastic_beanstalk.types.listener.Listener"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: LoadBalancerListenersDescription, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_beanstalk.types.listener

    for n, item in enumerate(value, 1):
        capo_elastic_beanstalk.types.listener.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> LoadBalancerListenersDescription:
    import capo_elastic_beanstalk.types.listener

    out: LoadBalancerListenersDescription = []
    for child in el.findall("member"):
        out.append(capo_elastic_beanstalk.types.listener.deserialize_query(child))
    return out


def serialize_query_flat(
    value: LoadBalancerListenersDescription, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_beanstalk.types.listener

    for n, item in enumerate(value, 1):
        capo_elastic_beanstalk.types.listener.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(
    parent: Element, tag: str
) -> LoadBalancerListenersDescription:
    import capo_elastic_beanstalk.types.listener

    out: LoadBalancerListenersDescription = []
    for child in parent.findall(tag):
        out.append(capo_elastic_beanstalk.types.listener.deserialize_query(child))
    return out
