"""Generated from Smithy shape ``com.amazonaws.ec2#SecurityGroupVpcAssociationState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

SecurityGroupVpcAssociationState: TypeAlias = Literal[
    "associating",
    "associated",
    "association-failed",
    "disassociating",
    "disassociated",
    "disassociation-failed",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "associating",
        "associated",
        "association-failed",
        "disassociating",
        "disassociated",
        "disassociation-failed",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "associating",
        "associated",
        "association-failed",
        "disassociating",
        "disassociated",
        "disassociation-failed",
    )
)


def to_ec2_query_text(value: SecurityGroupVpcAssociationState) -> str:
    return value


def from_ec2_query_text(text: str) -> SecurityGroupVpcAssociationState:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown SecurityGroupVpcAssociationState value: {text!r}"
        )
    return cast(SecurityGroupVpcAssociationState, text)


def serialize_ec2_query(
    value: SecurityGroupVpcAssociationState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> SecurityGroupVpcAssociationState:
    return from_ec2_query_text(el.text or "")
