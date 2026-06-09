"""Generated from Smithy shape ``com.amazonaws.ec2#VpcEncryptionControlState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

VpcEncryptionControlState: TypeAlias = Literal[
    "enforce-in-progress",
    "monitor-in-progress",
    "enforce-failed",
    "monitor-failed",
    "deleting",
    "deleted",
    "available",
    "creating",
    "delete-failed",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "enforce-in-progress",
        "monitor-in-progress",
        "enforce-failed",
        "monitor-failed",
        "deleting",
        "deleted",
        "available",
        "creating",
        "delete-failed",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "enforce-in-progress",
        "monitor-in-progress",
        "enforce-failed",
        "monitor-failed",
        "deleting",
        "deleted",
        "available",
        "creating",
        "delete-failed",
    )
)


def to_ec2_query_text(value: VpcEncryptionControlState) -> str:
    return value


def from_ec2_query_text(text: str) -> VpcEncryptionControlState:
    if text not in _VALUES:
        raise DeserializationError(f"unknown VpcEncryptionControlState value: {text!r}")
    return cast(VpcEncryptionControlState, text)


def serialize_ec2_query(
    value: VpcEncryptionControlState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> VpcEncryptionControlState:
    return from_ec2_query_text(el.text or "")
