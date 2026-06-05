"""Generated from Smithy shape ``com.amazonaws.ec2#GatewayAssociationState``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

GatewayAssociationState: TypeAlias = Literal[
    "associated",
    "not-associated",
    "associating",
    "disassociating",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "associated",
        "not-associated",
        "associating",
        "disassociating",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "associated",
        "not-associated",
        "associating",
        "disassociating",
    )
)


def to_ec2_query_text(value: GatewayAssociationState) -> str:
    return value


def from_ec2_query_text(text: str) -> GatewayAssociationState:
    if text not in _VALUES:
        raise DeserializationError(f"unknown GatewayAssociationState value: {text!r}")
    return cast(GatewayAssociationState, text)


def serialize_ec2_query(
    value: GatewayAssociationState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> GatewayAssociationState:
    return from_ec2_query_text(el.text or "")
