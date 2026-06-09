"""Generated from Smithy shape ``com.amazonaws.ec2#VirtualizationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

VirtualizationType: TypeAlias = Literal[
    "hvm",
    "paravirtual",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "hvm",
        "paravirtual",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "hvm",
        "paravirtual",
    )
)


def to_ec2_query_text(value: VirtualizationType) -> str:
    return value


def from_ec2_query_text(text: str) -> VirtualizationType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown VirtualizationType value: {text!r}")
    return cast(VirtualizationType, text)


def serialize_ec2_query(
    value: VirtualizationType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> VirtualizationType:
    return from_ec2_query_text(el.text or "")
