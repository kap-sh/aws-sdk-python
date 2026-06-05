"""Generated from Smithy shape ``com.amazonaws.ec2#ArchitectureType``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

ArchitectureType: TypeAlias = Literal[
    "i386",
    "x86_64",
    "arm64",
    "x86_64_mac",
    "arm64_mac",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "i386",
        "x86_64",
        "arm64",
        "x86_64_mac",
        "arm64_mac",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "i386",
        "x86_64",
        "arm64",
        "x86_64_mac",
        "arm64_mac",
    )
)


def to_ec2_query_text(value: ArchitectureType) -> str:
    return value


def from_ec2_query_text(text: str) -> ArchitectureType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ArchitectureType value: {text!r}")
    return cast(ArchitectureType, text)


def serialize_ec2_query(
    value: ArchitectureType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ArchitectureType:
    return from_ec2_query_text(el.text or "")
