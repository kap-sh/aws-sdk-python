"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#IpAddressType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element
from aws_sdk_elastic_load_balancing_v2.errors import DeserializationError

IpAddressType: TypeAlias = Literal[
    "ipv4",
    "dualstack",
    "dualstack-without-public-ipv4",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ipv4",
        "dualstack",
        "dualstack-without-public-ipv4",
    )
)


def to_query_text(value: IpAddressType) -> str:
    return value


def from_query_text(text: str) -> IpAddressType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown IpAddressType value: {text!r}")
    return cast(IpAddressType, text)


def serialize_query(
    value: IpAddressType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> IpAddressType:
    return from_query_text(el.text or "")
