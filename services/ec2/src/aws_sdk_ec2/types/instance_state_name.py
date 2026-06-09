"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceStateName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

InstanceStateName: TypeAlias = Literal[
    "pending",
    "running",
    "shutting-down",
    "terminated",
    "stopping",
    "stopped",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "pending",
        "running",
        "shutting-down",
        "terminated",
        "stopping",
        "stopped",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "pending",
        "running",
        "shutting-down",
        "terminated",
        "stopping",
        "stopped",
    )
)


def to_ec2_query_text(value: InstanceStateName) -> str:
    return value


def from_ec2_query_text(text: str) -> InstanceStateName:
    if text not in _VALUES:
        raise DeserializationError(f"unknown InstanceStateName value: {text!r}")
    return cast(InstanceStateName, text)


def serialize_ec2_query(
    value: InstanceStateName, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> InstanceStateName:
    return from_ec2_query_text(el.text or "")
