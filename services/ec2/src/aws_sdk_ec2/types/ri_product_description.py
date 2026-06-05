"""Generated from Smithy shape ``com.amazonaws.ec2#RIProductDescription``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

RIProductDescription: TypeAlias = Literal[
    "Linux/UNIX",
    "Linux/UNIX (Amazon VPC)",
    "Windows",
    "Windows (Amazon VPC)",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Linux/UNIX",
        "Linux/UNIX (Amazon VPC)",
        "Windows",
        "Windows (Amazon VPC)",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "Linux/UNIX",
        "Linux/UNIX (Amazon VPC)",
        "Windows",
        "Windows (Amazon VPC)",
    )
)


def to_ec2_query_text(value: RIProductDescription) -> str:
    return value


def from_ec2_query_text(text: str) -> RIProductDescription:
    if text not in _VALUES:
        raise DeserializationError(f"unknown RIProductDescription value: {text!r}")
    return cast(RIProductDescription, text)


def serialize_ec2_query(
    value: RIProductDescription, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> RIProductDescription:
    return from_ec2_query_text(el.text or "")
