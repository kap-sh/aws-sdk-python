"""Generated from Smithy shape ``com.amazonaws.ec2#ContainerFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

ContainerFormat: TypeAlias = Literal["ova",]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: ContainerFormat) -> str:
    return value


def from_ec2_query_text(text: str) -> ContainerFormat:
    return cast(ContainerFormat, text)


def serialize_ec2_query(
    value: ContainerFormat, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ContainerFormat:
    return from_ec2_query_text(el.text or "")
