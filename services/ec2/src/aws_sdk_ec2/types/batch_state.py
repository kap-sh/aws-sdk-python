"""Generated from Smithy shape ``com.amazonaws.ec2#BatchState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

BatchState: TypeAlias = Literal[
    "submitted",
    "active",
    "cancelled",
    "failed",
    "cancelled_running",
    "cancelled_terminating",
    "modifying",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "submitted",
        "active",
        "cancelled",
        "failed",
        "cancelled_running",
        "cancelled_terminating",
        "modifying",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "submitted",
        "active",
        "cancelled",
        "failed",
        "cancelled_running",
        "cancelled_terminating",
        "modifying",
    )
)


def to_ec2_query_text(value: BatchState) -> str:
    return value


def from_ec2_query_text(text: str) -> BatchState:
    if text not in _VALUES:
        raise DeserializationError(f"unknown BatchState value: {text!r}")
    return cast(BatchState, text)


def serialize_ec2_query(
    value: BatchState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> BatchState:
    return from_ec2_query_text(el.text or "")
