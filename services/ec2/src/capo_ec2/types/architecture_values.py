"""Generated from Smithy shape ``com.amazonaws.ec2#ArchitectureValues``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

ArchitectureValues: TypeAlias = Literal[
    "i386",
    "x86_64",
    "arm64",
    "x86_64_mac",
    "arm64_mac",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: ArchitectureValues) -> str:
    return value


def from_ec2_query_text(text: str) -> ArchitectureValues:
    return cast(ArchitectureValues, text)


def serialize_ec2_query(
    value: ArchitectureValues, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ArchitectureValues:
    return from_ec2_query_text(el.text or "")
