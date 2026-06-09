"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayAttachmentResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

TransitGatewayAttachmentResourceType: TypeAlias = Literal[
    "vpc",
    "vpn",
    "vpn-concentrator",
    "direct-connect-gateway",
    "connect",
    "peering",
    "tgw-peering",
    "network-function",
    "client-vpn",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "vpc",
        "vpn",
        "vpn-concentrator",
        "direct-connect-gateway",
        "connect",
        "peering",
        "tgw-peering",
        "network-function",
        "client-vpn",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "vpc",
        "vpn",
        "vpn-concentrator",
        "direct-connect-gateway",
        "connect",
        "peering",
        "tgw-peering",
        "network-function",
        "client-vpn",
    )
)


def to_ec2_query_text(value: TransitGatewayAttachmentResourceType) -> str:
    return value


def from_ec2_query_text(text: str) -> TransitGatewayAttachmentResourceType:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown TransitGatewayAttachmentResourceType value: {text!r}"
        )
    return cast(TransitGatewayAttachmentResourceType, text)


def serialize_ec2_query(
    value: TransitGatewayAttachmentResourceType,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> TransitGatewayAttachmentResourceType:
    return from_ec2_query_text(el.text or "")
