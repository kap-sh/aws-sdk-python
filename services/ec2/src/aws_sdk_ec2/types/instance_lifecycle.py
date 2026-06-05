"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceLifecycle``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

InstanceLifecycle: TypeAlias = Literal[
    "spot",
    "on-demand",
    "interruptible-capacity-reservation",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "spot",
        "on-demand",
        "interruptible-capacity-reservation",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "spot",
        "on-demand",
        "interruptible-capacity-reservation",
    )
)


def to_ec2_query_text(value: InstanceLifecycle) -> str:
    return value


def from_ec2_query_text(text: str) -> InstanceLifecycle:
    if text not in _VALUES:
        raise DeserializationError(f"unknown InstanceLifecycle value: {text!r}")
    return cast(InstanceLifecycle, text)


def serialize_ec2_query(
    value: InstanceLifecycle, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> InstanceLifecycle:
    return from_ec2_query_text(el.text or "")
