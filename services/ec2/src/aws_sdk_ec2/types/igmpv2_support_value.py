"""Generated from Smithy shape ``com.amazonaws.ec2#Igmpv2SupportValue``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

Igmpv2SupportValue: TypeAlias = Literal[
    "enable",
    "disable",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "enable",
        "disable",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "enable",
        "disable",
    )
)


def to_ec2_query_text(value: Igmpv2SupportValue) -> str:
    return value


def from_ec2_query_text(text: str) -> Igmpv2SupportValue:
    if text not in _VALUES:
        raise DeserializationError(f"unknown Igmpv2SupportValue value: {text!r}")
    return cast(Igmpv2SupportValue, text)


def serialize_ec2_query(
    value: Igmpv2SupportValue, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> Igmpv2SupportValue:
    return from_ec2_query_text(el.text or "")
