"""Generated from Smithy shape ``com.amazonaws.elasticache#IpDiscovery``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elasticache._protocol.xml import Element
from aws_sdk_elasticache.errors import DeserializationError

IpDiscovery: TypeAlias = Literal[
    "ipv4",
    "ipv6",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ipv4",
        "ipv6",
    )
)


def to_query_text(value: IpDiscovery) -> str:
    return value


def from_query_text(text: str) -> IpDiscovery:
    if text not in _VALUES:
        raise DeserializationError(f"unknown IpDiscovery value: {text!r}")
    return cast(IpDiscovery, text)


def serialize_query(
    value: IpDiscovery, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> IpDiscovery:
    return from_query_text(el.text or "")
