"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#TargetGroupIpAddressTypeEnum``."""

from typing import Literal, TypeAlias, cast

from capo_elastic_load_balancing_v2._protocol.xml import Element

TargetGroupIpAddressTypeEnum: TypeAlias = Literal[
    "ipv4",
    "ipv6",
]


# --- awsQuery ser/de ---
def to_query_text(value: TargetGroupIpAddressTypeEnum) -> str:
    return value


def from_query_text(text: str) -> TargetGroupIpAddressTypeEnum:
    return cast(TargetGroupIpAddressTypeEnum, text)


def serialize_query(
    value: TargetGroupIpAddressTypeEnum, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> TargetGroupIpAddressTypeEnum:
    return from_query_text(el.text or "")
