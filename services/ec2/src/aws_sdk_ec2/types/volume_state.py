"""Generated from Smithy shape ``com.amazonaws.ec2#VolumeState``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

VolumeState: TypeAlias = Literal[
    "creating",
    "available",
    "in-use",
    "deleting",
    "deleted",
    "error",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "creating",
        "available",
        "in-use",
        "deleting",
        "deleted",
        "error",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "creating",
        "available",
        "in-use",
        "deleting",
        "deleted",
        "error",
    )
)


def to_ec2_query_text(value: VolumeState) -> str:
    return value


def from_ec2_query_text(text: str) -> VolumeState:
    if text not in _VALUES:
        raise DeserializationError(f"unknown VolumeState value: {text!r}")
    return cast(VolumeState, text)


def serialize_ec2_query(
    value: VolumeState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> VolumeState:
    return from_ec2_query_text(el.text or "")
