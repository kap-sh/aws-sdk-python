"""Generated from Smithy shape ``com.amazonaws.ec2#AutoPlacement``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

AutoPlacement: TypeAlias = Literal[
    "on",
    "off",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: AutoPlacement) -> str:
    return value


def from_ec2_query_text(text: str) -> AutoPlacement:
    return cast(AutoPlacement, text)


def serialize_ec2_query(
    value: AutoPlacement, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> AutoPlacement:
    return from_ec2_query_text(el.text or "")
