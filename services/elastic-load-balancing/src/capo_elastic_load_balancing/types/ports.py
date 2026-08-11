"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#Ports``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing.types.access_point_port

Ports: TypeAlias = list[
    "capo_elastic_load_balancing.types.access_point_port.AccessPointPort"
]


# --- awsQuery ser/de ---
def serialize_query(value: Ports, pairs: list[tuple[str, str]], prefix: str) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.member.{n}", str(item)))


def deserialize_query(el: Element) -> Ports:
    out: Ports = []
    for child in el.findall("member"):
        out.append(int(child.text or ""))
    return out


def serialize_query_flat(
    value: Ports, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(parent: Element, tag: str) -> Ports:
    out: Ports = []
    for child in parent.findall(tag):
        out.append(int(child.text or ""))
    return out
