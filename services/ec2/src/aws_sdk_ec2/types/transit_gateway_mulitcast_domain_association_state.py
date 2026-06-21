"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayMulitcastDomainAssociationState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

TransitGatewayMulitcastDomainAssociationState: TypeAlias = Literal[
    "pendingAcceptance",
    "associating",
    "associated",
    "disassociating",
    "disassociated",
    "rejected",
    "failed",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: TransitGatewayMulitcastDomainAssociationState) -> str:
    return value


def from_ec2_query_text(text: str) -> TransitGatewayMulitcastDomainAssociationState:
    return cast(TransitGatewayMulitcastDomainAssociationState, text)


def serialize_ec2_query(
    value: TransitGatewayMulitcastDomainAssociationState,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> TransitGatewayMulitcastDomainAssociationState:
    return from_ec2_query_text(el.text or "")
