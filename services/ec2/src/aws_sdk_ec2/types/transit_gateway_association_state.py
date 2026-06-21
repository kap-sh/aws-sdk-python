"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayAssociationState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

TransitGatewayAssociationState: TypeAlias = Literal[
    "associating",
    "associated",
    "disassociating",
    "disassociated",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: TransitGatewayAssociationState) -> str:
    return value


def from_ec2_query_text(text: str) -> TransitGatewayAssociationState:
    return cast(TransitGatewayAssociationState, text)


def serialize_ec2_query(
    value: TransitGatewayAssociationState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> TransitGatewayAssociationState:
    return from_ec2_query_text(el.text or "")
