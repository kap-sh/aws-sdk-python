"""Generated from Smithy shape ``com.amazonaws.elasticache#IpDiscovery``."""

from typing import Literal, TypeAlias, cast

from capo_elasticache._protocol.xml import Element

IpDiscovery: TypeAlias = Literal[
    "ipv4",
    "ipv6",
]


# --- awsQuery ser/de ---
def to_query_text(value: IpDiscovery) -> str:
    return value


def from_query_text(text: str) -> IpDiscovery:
    return cast(IpDiscovery, text)


def serialize_query(
    value: IpDiscovery, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> IpDiscovery:
    return from_query_text(el.text or "")
