"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceMatchCriteria``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

InstanceMatchCriteria: TypeAlias = Literal[
    "open",
    "targeted",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: InstanceMatchCriteria) -> str:
    return value


def from_ec2_query_text(text: str) -> InstanceMatchCriteria:
    return cast(InstanceMatchCriteria, text)


def serialize_ec2_query(
    value: InstanceMatchCriteria, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> InstanceMatchCriteria:
    return from_ec2_query_text(el.text or "")
