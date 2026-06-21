"""Generated from Smithy shape ``com.amazonaws.ec2#PartitionLoadFrequency``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

PartitionLoadFrequency: TypeAlias = Literal[
    "none",
    "daily",
    "weekly",
    "monthly",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: PartitionLoadFrequency) -> str:
    return value


def from_ec2_query_text(text: str) -> PartitionLoadFrequency:
    return cast(PartitionLoadFrequency, text)


def serialize_ec2_query(
    value: PartitionLoadFrequency, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> PartitionLoadFrequency:
    return from_ec2_query_text(el.text or "")
