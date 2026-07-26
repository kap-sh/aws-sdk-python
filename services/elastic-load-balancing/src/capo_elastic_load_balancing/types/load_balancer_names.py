"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#LoadBalancerNames``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing.types.access_point_name

LoadBalancerNames: TypeAlias = list[
    "capo_elastic_load_balancing.types.access_point_name.AccessPointName"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: LoadBalancerNames, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.member.{n}", str(item)))


def deserialize_query(el: Element) -> LoadBalancerNames:
    out: LoadBalancerNames = []
    for child in el.findall("member"):
        out.append(str(child.text or ""))
    return out


def serialize_query_flat(
    value: LoadBalancerNames, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(parent: Element, tag: str) -> LoadBalancerNames:
    out: LoadBalancerNames = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
