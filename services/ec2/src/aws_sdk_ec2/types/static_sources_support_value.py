"""Generated from Smithy shape ``com.amazonaws.ec2#StaticSourcesSupportValue``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

StaticSourcesSupportValue: TypeAlias = Literal[
    "enable",
    "disable",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: StaticSourcesSupportValue) -> str:
    return value


def from_ec2_query_text(text: str) -> StaticSourcesSupportValue:
    return cast(StaticSourcesSupportValue, text)


def serialize_ec2_query(
    value: StaticSourcesSupportValue, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> StaticSourcesSupportValue:
    return from_ec2_query_text(el.text or "")
