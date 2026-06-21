"""Generated from Smithy shape ``com.amazonaws.ec2#AsnAssociationState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

AsnAssociationState: TypeAlias = Literal[
    "disassociated",
    "failed-disassociation",
    "failed-association",
    "pending-disassociation",
    "pending-association",
    "associated",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: AsnAssociationState) -> str:
    return value


def from_ec2_query_text(text: str) -> AsnAssociationState:
    return cast(AsnAssociationState, text)


def serialize_ec2_query(
    value: AsnAssociationState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> AsnAssociationState:
    return from_ec2_query_text(el.text or "")
