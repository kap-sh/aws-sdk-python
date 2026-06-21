"""Generated from Smithy shape ``com.amazonaws.ec2#ArchitectureType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

ArchitectureType: TypeAlias = Literal[
    "i386",
    "x86_64",
    "arm64",
    "x86_64_mac",
    "arm64_mac",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: ArchitectureType) -> str:
    return value


def from_ec2_query_text(text: str) -> ArchitectureType:
    return cast(ArchitectureType, text)


def serialize_ec2_query(
    value: ArchitectureType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ArchitectureType:
    return from_ec2_query_text(el.text or "")
