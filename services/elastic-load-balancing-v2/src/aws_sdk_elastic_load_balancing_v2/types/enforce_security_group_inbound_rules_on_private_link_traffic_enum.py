"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#EnforceSecurityGroupInboundRulesOnPrivateLinkTrafficEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

EnforceSecurityGroupInboundRulesOnPrivateLinkTrafficEnum: TypeAlias = Literal[
    "on",
    "off",
]


# --- awsQuery ser/de ---
def to_query_text(
    value: EnforceSecurityGroupInboundRulesOnPrivateLinkTrafficEnum,
) -> str:
    return value


def from_query_text(
    text: str,
) -> EnforceSecurityGroupInboundRulesOnPrivateLinkTrafficEnum:
    return cast(EnforceSecurityGroupInboundRulesOnPrivateLinkTrafficEnum, text)


def serialize_query(
    value: EnforceSecurityGroupInboundRulesOnPrivateLinkTrafficEnum,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(
    el: Element,
) -> EnforceSecurityGroupInboundRulesOnPrivateLinkTrafficEnum:
    return from_query_text(el.text or "")
