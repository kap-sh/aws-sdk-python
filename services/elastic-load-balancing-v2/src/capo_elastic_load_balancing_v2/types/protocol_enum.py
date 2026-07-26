"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#ProtocolEnum``."""

from typing import Literal, TypeAlias, cast

from capo_elastic_load_balancing_v2._protocol.xml import Element

ProtocolEnum: TypeAlias = Literal[
    "HTTP",
    "HTTPS",
    "TCP",
    "TLS",
    "UDP",
    "TCP_UDP",
    "GENEVE",
    "QUIC",
    "TCP_QUIC",
]


# --- awsQuery ser/de ---
def to_query_text(value: ProtocolEnum) -> str:
    return value


def from_query_text(text: str) -> ProtocolEnum:
    return cast(ProtocolEnum, text)


def serialize_query(
    value: ProtocolEnum, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ProtocolEnum:
    return from_query_text(el.text or "")
