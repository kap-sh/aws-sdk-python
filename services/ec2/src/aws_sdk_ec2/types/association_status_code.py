"""Generated from Smithy shape ``com.amazonaws.ec2#AssociationStatusCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

AssociationStatusCode: TypeAlias = Literal[
    "associating",
    "associated",
    "association-failed",
    "disassociating",
    "disassociated",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "associating",
        "associated",
        "association-failed",
        "disassociating",
        "disassociated",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "associating",
        "associated",
        "association-failed",
        "disassociating",
        "disassociated",
    )
)


def to_ec2_query_text(value: AssociationStatusCode) -> str:
    return value


def from_ec2_query_text(text: str) -> AssociationStatusCode:
    if text not in _VALUES:
        raise DeserializationError(f"unknown AssociationStatusCode value: {text!r}")
    return cast(AssociationStatusCode, text)


def serialize_ec2_query(
    value: AssociationStatusCode, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> AssociationStatusCode:
    return from_ec2_query_text(el.text or "")
