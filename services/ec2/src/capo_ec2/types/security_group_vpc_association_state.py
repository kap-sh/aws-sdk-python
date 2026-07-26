"""Generated from Smithy shape ``com.amazonaws.ec2#SecurityGroupVpcAssociationState``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

SecurityGroupVpcAssociationState: TypeAlias = Literal[
    "associating",
    "associated",
    "association-failed",
    "disassociating",
    "disassociated",
    "disassociation-failed",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: SecurityGroupVpcAssociationState) -> str:
    return value


def from_ec2_query_text(text: str) -> SecurityGroupVpcAssociationState:
    return cast(SecurityGroupVpcAssociationState, text)


def serialize_ec2_query(
    value: SecurityGroupVpcAssociationState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> SecurityGroupVpcAssociationState:
    return from_ec2_query_text(el.text or "")
