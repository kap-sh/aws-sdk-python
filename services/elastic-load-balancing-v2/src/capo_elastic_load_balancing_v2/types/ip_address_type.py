"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#IpAddressType``."""

from typing import Literal, TypeAlias, cast

from capo_elastic_load_balancing_v2._protocol.xml import Element

IpAddressType: TypeAlias = Literal[
    "ipv4",
    "dualstack",
    "dualstack-without-public-ipv4",
]


# --- awsQuery ser/de ---
def to_query_text(value: IpAddressType) -> str:
    return value


def from_query_text(text: str) -> IpAddressType:
    return cast(IpAddressType, text)


def serialize_query(
    value: IpAddressType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> IpAddressType:
    return from_query_text(el.text or "")
