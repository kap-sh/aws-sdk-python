"""Generated from Smithy shape ``com.amazonaws.ec2#VpnState``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

VpnState: TypeAlias = Literal[
    "pending",
    "available",
    "deleting",
    "deleted",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "pending",
        "available",
        "deleting",
        "deleted",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "pending",
        "available",
        "deleting",
        "deleted",
    )
)


def to_ec2_query_text(value: VpnState) -> str:
    return value


def from_ec2_query_text(text: str) -> VpnState:
    if text not in _VALUES:
        raise DeserializationError(f"unknown VpnState value: {text!r}")
    return cast(VpnState, text)


def serialize_ec2_query(
    value: VpnState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> VpnState:
    return from_ec2_query_text(el.text or "")
