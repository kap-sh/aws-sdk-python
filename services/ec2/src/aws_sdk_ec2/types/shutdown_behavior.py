"""Generated from Smithy shape ``com.amazonaws.ec2#ShutdownBehavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

ShutdownBehavior: TypeAlias = Literal[
    "stop",
    "terminate",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "stop",
        "terminate",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "stop",
        "terminate",
    )
)


def to_ec2_query_text(value: ShutdownBehavior) -> str:
    return value


def from_ec2_query_text(text: str) -> ShutdownBehavior:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ShutdownBehavior value: {text!r}")
    return cast(ShutdownBehavior, text)


def serialize_ec2_query(
    value: ShutdownBehavior, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ShutdownBehavior:
    return from_ec2_query_text(el.text or "")
