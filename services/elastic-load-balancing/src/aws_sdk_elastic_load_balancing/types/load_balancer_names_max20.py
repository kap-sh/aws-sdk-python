"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#LoadBalancerNamesMax20``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing.types.access_point_name

LoadBalancerNamesMax20: TypeAlias = list[
    "aws_sdk_elastic_load_balancing.types.access_point_name.AccessPointName"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: LoadBalancerNamesMax20, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.member.{n}", str(item)))


def deserialize_query(el: Element) -> LoadBalancerNamesMax20:
    out: LoadBalancerNamesMax20 = []
    for child in el.findall("member"):
        out.append(str(child.text or ""))
    return out


def serialize_query_flat(
    value: LoadBalancerNamesMax20, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(parent: Element, tag: str) -> LoadBalancerNamesMax20:
    out: LoadBalancerNamesMax20 = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
