"""Generated from Smithy shape ``com.amazonaws.ec2#VpcCidrBlockStateCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

VpcCidrBlockStateCode: TypeAlias = Literal[
    "associating",
    "associated",
    "disassociating",
    "disassociated",
    "failing",
    "failed",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "associating",
        "associated",
        "disassociating",
        "disassociated",
        "failing",
        "failed",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "associating",
        "associated",
        "disassociating",
        "disassociated",
        "failing",
        "failed",
    )
)


def to_ec2_query_text(value: VpcCidrBlockStateCode) -> str:
    return value


def from_ec2_query_text(text: str) -> VpcCidrBlockStateCode:
    if text not in _VALUES:
        raise DeserializationError(f"unknown VpcCidrBlockStateCode value: {text!r}")
    return cast(VpcCidrBlockStateCode, text)


def serialize_ec2_query(
    value: VpcCidrBlockStateCode, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> VpcCidrBlockStateCode:
    return from_ec2_query_text(el.text or "")
