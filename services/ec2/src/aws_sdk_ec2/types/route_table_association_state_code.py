"""Generated from Smithy shape ``com.amazonaws.ec2#RouteTableAssociationStateCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

RouteTableAssociationStateCode: TypeAlias = Literal[
    "associating",
    "associated",
    "disassociating",
    "disassociated",
    "failed",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "associating",
        "associated",
        "disassociating",
        "disassociated",
        "failed",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "associating",
        "associated",
        "disassociating",
        "disassociated",
        "failed",
    )
)


def to_ec2_query_text(value: RouteTableAssociationStateCode) -> str:
    return value


def from_ec2_query_text(text: str) -> RouteTableAssociationStateCode:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown RouteTableAssociationStateCode value: {text!r}"
        )
    return cast(RouteTableAssociationStateCode, text)


def serialize_ec2_query(
    value: RouteTableAssociationStateCode, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> RouteTableAssociationStateCode:
    return from_ec2_query_text(el.text or "")
