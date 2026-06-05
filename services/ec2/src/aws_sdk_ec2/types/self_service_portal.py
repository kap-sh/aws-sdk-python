"""Generated from Smithy shape ``com.amazonaws.ec2#SelfServicePortal``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

SelfServicePortal: TypeAlias = Literal[
    "enabled",
    "disabled",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "enabled",
        "disabled",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "enabled",
        "disabled",
    )
)


def to_ec2_query_text(value: SelfServicePortal) -> str:
    return value


def from_ec2_query_text(text: str) -> SelfServicePortal:
    if text not in _VALUES:
        raise DeserializationError(f"unknown SelfServicePortal value: {text!r}")
    return cast(SelfServicePortal, text)


def serialize_ec2_query(
    value: SelfServicePortal, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> SelfServicePortal:
    return from_ec2_query_text(el.text or "")
