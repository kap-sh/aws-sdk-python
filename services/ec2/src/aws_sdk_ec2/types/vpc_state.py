"""Generated from Smithy shape ``com.amazonaws.ec2#VpcState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

VpcState: TypeAlias = Literal[
    "pending",
    "available",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "pending",
        "available",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "pending",
        "available",
    )
)


def to_ec2_query_text(value: VpcState) -> str:
    return value


def from_ec2_query_text(text: str) -> VpcState:
    if text not in _VALUES:
        raise DeserializationError(f"unknown VpcState value: {text!r}")
    return cast(VpcState, text)


def serialize_ec2_query(
    value: VpcState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> VpcState:
    return from_ec2_query_text(el.text or "")
