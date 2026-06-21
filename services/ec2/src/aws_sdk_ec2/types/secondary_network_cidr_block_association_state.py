"""Generated from Smithy shape ``com.amazonaws.ec2#SecondaryNetworkCidrBlockAssociationState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

SecondaryNetworkCidrBlockAssociationState: TypeAlias = Literal[
    "associating",
    "associated",
    "association-failed",
    "disassociating",
    "disassociated",
    "disassociation-failed",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: SecondaryNetworkCidrBlockAssociationState) -> str:
    return value


def from_ec2_query_text(text: str) -> SecondaryNetworkCidrBlockAssociationState:
    return cast(SecondaryNetworkCidrBlockAssociationState, text)


def serialize_ec2_query(
    value: SecondaryNetworkCidrBlockAssociationState,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> SecondaryNetworkCidrBlockAssociationState:
    return from_ec2_query_text(el.text or "")
