"""Generated from Smithy shape ``com.amazonaws.ec2#VpcEncryptionControlMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

VpcEncryptionControlMode: TypeAlias = Literal[
    "monitor",
    "enforce",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "monitor",
        "enforce",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "monitor",
        "enforce",
    )
)


def to_ec2_query_text(value: VpcEncryptionControlMode) -> str:
    return value


def from_ec2_query_text(text: str) -> VpcEncryptionControlMode:
    if text not in _VALUES:
        raise DeserializationError(f"unknown VpcEncryptionControlMode value: {text!r}")
    return cast(VpcEncryptionControlMode, text)


def serialize_ec2_query(
    value: VpcEncryptionControlMode, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> VpcEncryptionControlMode:
    return from_ec2_query_text(el.text or "")
