"""Generated from Smithy shape ``com.amazonaws.ec2#scope``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

scope: TypeAlias = Literal[
    "Availability Zone",
    "Region",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Availability Zone",
        "Region",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "Availability Zone",
        "Region",
    )
)


def to_ec2_query_text(value: scope) -> str:
    return value


def from_ec2_query_text(text: str) -> scope:
    if text not in _VALUES:
        raise DeserializationError(f"unknown scope value: {text!r}")
    return cast(scope, text)


def serialize_ec2_query(
    value: scope, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> scope:
    return from_ec2_query_text(el.text or "")
