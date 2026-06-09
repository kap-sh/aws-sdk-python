"""Generated from Smithy shape ``com.amazonaws.ec2#SecondarySubnetCidrBlockAssociationState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

SecondarySubnetCidrBlockAssociationState: TypeAlias = Literal[
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


def to_ec2_query_text(value: SecondarySubnetCidrBlockAssociationState) -> str:
    return value


def from_ec2_query_text(text: str) -> SecondarySubnetCidrBlockAssociationState:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown SecondarySubnetCidrBlockAssociationState value: {text!r}"
        )
    return cast(SecondarySubnetCidrBlockAssociationState, text)


def serialize_ec2_query(
    value: SecondarySubnetCidrBlockAssociationState,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> SecondarySubnetCidrBlockAssociationState:
    return from_ec2_query_text(el.text or "")
