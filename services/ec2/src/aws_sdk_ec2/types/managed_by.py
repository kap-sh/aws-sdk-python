"""Generated from Smithy shape ``com.amazonaws.ec2#ManagedBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

ManagedBy: TypeAlias = Literal[
    "account",
    "declarative-policy",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "account",
        "declarative-policy",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "account",
        "declarative-policy",
    )
)


def to_ec2_query_text(value: ManagedBy) -> str:
    return value


def from_ec2_query_text(text: str) -> ManagedBy:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ManagedBy value: {text!r}")
    return cast(ManagedBy, text)


def serialize_ec2_query(
    value: ManagedBy, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ManagedBy:
    return from_ec2_query_text(el.text or "")
