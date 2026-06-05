"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceEventWindowState``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

InstanceEventWindowState: TypeAlias = Literal[
    "creating",
    "deleting",
    "active",
    "deleted",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "creating",
        "deleting",
        "active",
        "deleted",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "creating",
        "deleting",
        "active",
        "deleted",
    )
)


def to_ec2_query_text(value: InstanceEventWindowState) -> str:
    return value


def from_ec2_query_text(text: str) -> InstanceEventWindowState:
    if text not in _VALUES:
        raise DeserializationError(f"unknown InstanceEventWindowState value: {text!r}")
    return cast(InstanceEventWindowState, text)


def serialize_ec2_query(
    value: InstanceEventWindowState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> InstanceEventWindowState:
    return from_ec2_query_text(el.text or "")
