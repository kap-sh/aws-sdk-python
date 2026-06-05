"""Generated from Smithy shape ``com.amazonaws.ec2#VolumeAttachmentState``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

VolumeAttachmentState: TypeAlias = Literal[
    "attaching",
    "attached",
    "detaching",
    "detached",
    "busy",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "attaching",
        "attached",
        "detaching",
        "detached",
        "busy",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "attaching",
        "attached",
        "detaching",
        "detached",
        "busy",
    )
)


def to_ec2_query_text(value: VolumeAttachmentState) -> str:
    return value


def from_ec2_query_text(text: str) -> VolumeAttachmentState:
    if text not in _VALUES:
        raise DeserializationError(f"unknown VolumeAttachmentState value: {text!r}")
    return cast(VolumeAttachmentState, text)


def serialize_ec2_query(
    value: VolumeAttachmentState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> VolumeAttachmentState:
    return from_ec2_query_text(el.text or "")
