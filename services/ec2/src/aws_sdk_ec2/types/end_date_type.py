"""Generated from Smithy shape ``com.amazonaws.ec2#EndDateType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

EndDateType: TypeAlias = Literal[
    "unlimited",
    "limited",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: EndDateType) -> str:
    return value


def from_ec2_query_text(text: str) -> EndDateType:
    return cast(EndDateType, text)


def serialize_ec2_query(
    value: EndDateType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> EndDateType:
    return from_ec2_query_text(el.text or "")
