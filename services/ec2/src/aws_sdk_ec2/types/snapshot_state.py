"""Generated from Smithy shape ``com.amazonaws.ec2#SnapshotState``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

SnapshotState: TypeAlias = Literal[
    "pending",
    "completed",
    "error",
    "recoverable",
    "recovering",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "pending",
        "completed",
        "error",
        "recoverable",
        "recovering",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "pending",
        "completed",
        "error",
        "recoverable",
        "recovering",
    )
)


def to_ec2_query_text(value: SnapshotState) -> str:
    return value


def from_ec2_query_text(text: str) -> SnapshotState:
    if text not in _VALUES:
        raise DeserializationError(f"unknown SnapshotState value: {text!r}")
    return cast(SnapshotState, text)


def serialize_ec2_query(
    value: SnapshotState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> SnapshotState:
    return from_ec2_query_text(el.text or "")
