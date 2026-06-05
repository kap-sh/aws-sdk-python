"""Generated from Smithy shape ``com.amazonaws.ec2#MacModificationTaskState``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

MacModificationTaskState: TypeAlias = Literal[
    "successful",
    "failed",
    "in-progress",
    "pending",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "successful",
        "failed",
        "in-progress",
        "pending",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "successful",
        "failed",
        "in-progress",
        "pending",
    )
)


def to_ec2_query_text(value: MacModificationTaskState) -> str:
    return value


def from_ec2_query_text(text: str) -> MacModificationTaskState:
    if text not in _VALUES:
        raise DeserializationError(f"unknown MacModificationTaskState value: {text!r}")
    return cast(MacModificationTaskState, text)


def serialize_ec2_query(
    value: MacModificationTaskState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> MacModificationTaskState:
    return from_ec2_query_text(el.text or "")
