"""Generated from Smithy shape ``com.amazonaws.ec2#RIProductDescription``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

RIProductDescription: TypeAlias = Literal[
    "Linux/UNIX",
    "Linux/UNIX (Amazon VPC)",
    "Windows",
    "Windows (Amazon VPC)",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: RIProductDescription) -> str:
    return value


def from_ec2_query_text(text: str) -> RIProductDescription:
    return cast(RIProductDescription, text)


def serialize_ec2_query(
    value: RIProductDescription, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> RIProductDescription:
    return from_ec2_query_text(el.text or "")
