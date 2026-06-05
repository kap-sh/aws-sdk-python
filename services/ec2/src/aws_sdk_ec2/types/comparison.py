"""Generated from Smithy shape ``com.amazonaws.ec2#Comparison``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

Comparison: TypeAlias = Literal[
    "equals",
    "in",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "equals",
        "in",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "equals",
        "in",
    )
)


def to_ec2_query_text(value: Comparison) -> str:
    return value


def from_ec2_query_text(text: str) -> Comparison:
    if text not in _VALUES:
        raise DeserializationError(f"unknown Comparison value: {text!r}")
    return cast(Comparison, text)


def serialize_ec2_query(
    value: Comparison, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> Comparison:
    return from_ec2_query_text(el.text or "")
