"""Generated from Smithy shape ``com.amazonaws.ec2#ActivityStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

ActivityStatus: TypeAlias = Literal[
    "error",
    "pending_fulfillment",
    "pending_termination",
    "fulfilled",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "error",
        "pending_fulfillment",
        "pending_termination",
        "fulfilled",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "error",
        "pending_fulfillment",
        "pending_termination",
        "fulfilled",
    )
)


def to_ec2_query_text(value: ActivityStatus) -> str:
    return value


def from_ec2_query_text(text: str) -> ActivityStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ActivityStatus value: {text!r}")
    return cast(ActivityStatus, text)


def serialize_ec2_query(
    value: ActivityStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ActivityStatus:
    return from_ec2_query_text(el.text or "")
