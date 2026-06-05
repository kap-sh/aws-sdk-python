"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceAutoRecoveryState``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

InstanceAutoRecoveryState: TypeAlias = Literal[
    "disabled",
    "default",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "disabled",
        "default",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "disabled",
        "default",
    )
)


def to_ec2_query_text(value: InstanceAutoRecoveryState) -> str:
    return value


def from_ec2_query_text(text: str) -> InstanceAutoRecoveryState:
    if text not in _VALUES:
        raise DeserializationError(f"unknown InstanceAutoRecoveryState value: {text!r}")
    return cast(InstanceAutoRecoveryState, text)


def serialize_ec2_query(
    value: InstanceAutoRecoveryState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> InstanceAutoRecoveryState:
    return from_ec2_query_text(el.text or "")
