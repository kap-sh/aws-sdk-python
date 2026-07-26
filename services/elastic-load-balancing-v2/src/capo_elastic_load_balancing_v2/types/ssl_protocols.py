"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#SslProtocols``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.ssl_protocol

SslProtocols: TypeAlias = list[
    "capo_elastic_load_balancing_v2.types.ssl_protocol.SslProtocol"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: SslProtocols, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.member.{n}", str(item)))


def deserialize_query(el: Element) -> SslProtocols:
    out: SslProtocols = []
    for child in el.findall("member"):
        out.append(str(child.text or ""))
    return out


def serialize_query_flat(
    value: SslProtocols, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(parent: Element, tag: str) -> SslProtocols:
    out: SslProtocols = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
